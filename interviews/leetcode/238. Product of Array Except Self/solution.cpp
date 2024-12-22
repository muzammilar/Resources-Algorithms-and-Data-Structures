class Solution
{
  public:
	vector<int> productExceptSelf(const vector<int> &nums) {
		int n = nums.size();
		vector<int> answer(n, 1);

		// Step 1: Compute prefix products
		int prefix = 1;
		for (int i = 0; i < n; ++i) {
			answer[i] = prefix;
			prefix *= nums[i];
		}

		// Step 2: Compute postfix products and multiply with prefix
		int postfix = 1;
		for (int i = n - 1; i >= 0; --i) {
			answer[i] *= postfix;
			postfix *= nums[i];
		}

		return answer;
	}
};

/*
int main() {
	// Test cases
	vector<int> nums1 = {1, 2, 3, 4};
	vector<int> result1 = productExceptSelf(nums1);
	for (int num : result1) cout << num << " "; // Output: 24 12 8 6
	cout << endl;

	vector<int> nums2 = {-1, 1, 0, -3, 3};
	vector<int> result2 = productExceptSelf(nums2);
	for (int num : result2) cout << num << " "; // Output: 0 0 9 0 0
	cout << endl;

	return 0;
}
*/
