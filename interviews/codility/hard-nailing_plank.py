def solution(A, B, C):
    MM = 2 * len(C) + 1
    min_start = min(A)
    max_end = max(B)
    plank = namedtuple('P', ['start', 'end'])

    # 1: remove all wrapping planks
    #  x----------x  | remove in step 1.1
    #  x------x      | remove in step 1.2
    #    x--x        | keep
    # 1.1 starting at the same point as smaller plank
    starts = {}
    for a, b in izip(A, B):
        if a not in starts or b < starts[a].end:
            starts[a] = plank(a, b)

    # 1.2 starting before and ending after other (smaller) plank
    stack = []
    for i in xrange(min_start, max_end + 1):
        if i not in starts:
            continue
        plank = starts[i]
        while stack and plank.end <= stack[-1].end:
            stack.pop()
        stack.append(plank)

    # 2: Initialise dictionaries:
    #    plank_starts: start [key] to index Plank(start, end) [value]
    #    plank_ends: end [key] to index Plank(start, end) [value]
    #    nail_pos: nail position [key, C[i]] to index minimum nail index [value, i]
    plank_starts = {}
    plank_ends = {}
    for plank in stack:
        plank_starts[plank.start] = plank
        plank_ends[plank.end] = plank

    nail_pos = defaultdict(lambda: MM)
    for idx, pos in enumerate(C):
        if pos >= min_start and pos <= max_end:
            nail_pos[pos] = min(idx, nail_pos[pos])

    # 3: Traverse all positions between minimum plank start
    #    and maximum plank end (inclusive).
    # Result holds running maximum of best (smallest) nail index for each plank.
    result = -1
    # Keep track of minimum valid nail index for plank
    nail_plank = defaultdict(lambda: MM)
    # Keep overlapping planks in queue
    q = deque()

    positions = set().union(plank_starts, plank_ends, nail_pos)
    for i in xrange(min_start, max_end + 1):
        # There is nothing happening at i, so continue
        if i not in positions:
            continue
        # We are in the gap between planks, so continue
        if not q and i not in plank_starts:
            continue

        # New plank starts at position i
        if i in plank_starts:
            plank = plank_starts[i]
            # pop previous, active planks if they don't have nails yet
            if q:
                last = q[-1]
                if last not in nail_plank:
                    q.pop()
            q.append(plank)

        # Nail located at position i
        if i in nail_pos:
            plank = q.pop()
            nail = nail_pos[i]
            # set this nail if new for plank or better than previous
            nail_plank[plank] = min(nail, nail_plank[plank])
            while q:
                last = q[-1]
                # pop all previous planks with worse nail
                if last in nail_plank and nail_plank[last] >= nail:
                    q.pop()
                else:
                    break
            q.append(plank)

        # Plank ends at position i, let's make sure it's found a nail
        if i in plank_ends:
            # print 'End'
            plank = plank_ends[i]
            # Look up minimum valid nail index for plank
            min_nail_plank = q[0]

            if min_nail_plank not in nail_plank:
                return -1

            nail = nail_plank[min_nail_plank]
            result = max(nail, result)

            if plank == q[0]:
                q.popleft()

    return result + 1
    
    
"""


You are given two non-empty zero-indexed arrays A and B consisting of N integers. These arrays represent N planks. More precisely, A[K] is the start and B[K] the end of the K−th plank.

Next, you are given a non-empty zero-indexed array C consisting of M integers. This array represents M nails. More precisely, C[I] is the position where you can hammer in the I−th nail.

We say that a plank (A[K], B[K]) is nailed if there exists a nail C[I] such that A[K] ≤ C[I] ≤ B[K].

The goal is to find the minimum number of nails that must be used until all the planks are nailed. In other words, you should find a value J such that all planks will be nailed after using only the first J nails. More precisely, for every plank (A[K], B[K]) such that 0 ≤ K < N, there should exist a nail C[I] such that I < J and A[K] ≤ C[I] ≤ B[K].

For example, given arrays A, B such that:
    A[0] = 1    B[0] = 4
    A[1] = 4    B[1] = 5
    A[2] = 5    B[2] = 9
    A[3] = 8    B[3] = 10

four planks are represented: [1, 4], [4, 5], [5, 9] and [8, 10].

Given array C such that:
    C[0] = 4
    C[1] = 6
    C[2] = 7
    C[3] = 10
    C[4] = 2

if we use the following nails:

        0, then planks [1, 4] and [4, 5] will both be nailed.
        0, 1, then planks [1, 4], [4, 5] and [5, 9] will be nailed.
        0, 1, 2, then planks [1, 4], [4, 5] and [5, 9] will be nailed.
        0, 1, 2, 3, then all the planks will be nailed.

Thus, four is the minimum number of nails that, used sequentially, allow all the planks to be nailed.

Write a function:

    int solution(int A[], int B[], int N, int C[], int M);

that, given two non-empty zero-indexed arrays A and B consisting of N integers and a non-empty zero-indexed array C consisting of M integers, returns the minimum number of nails that, used sequentially, allow all the planks to be nailed.

If it is not possible to nail all the planks, the function should return −1.

For example, given arrays A, B, C such that:
    A[0] = 1    B[0] = 4
    A[1] = 4    B[1] = 5
    A[2] = 5    B[2] = 9
    A[3] = 8    B[3] = 10

    C[0] = 4
    C[1] = 6
    C[2] = 7
    C[3] = 10
    C[4] = 2

the function should return 4, as explained above.

Assume that:

        N and M are integers within the range [1..30,000];
        each element of arrays A, B, C is an integer within the range [1..2*M];
        A[K] ≤ B[K].

Complexity:

        expected worst-case time complexity is O((N+M)*log(M));
        expected worst-case space complexity is O(M), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.


"""