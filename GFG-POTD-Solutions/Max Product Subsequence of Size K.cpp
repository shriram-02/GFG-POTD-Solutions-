class Solution {
  public:
    int maxProduct(vector<int> &arr, int k) {

        int n = arr.size();

        // Sort the array.
        sort(arr.begin(), arr.end());

        // Store the maximum product.
        int product = 1;

        // If the largest element is 0 and k is odd.
        if (arr[n - 1] == 0 && (k & 1)) {
            return 0;
        }

        // If all elements are non-positive and k is odd.
        if (arr[n - 1] <= 0 && (k & 1)) {

            for (int i = n - 1; i >= n - k; i--) {
                product *= arr[i];
            }

            return product;
        }

        int left = 0;
        int right = n - 1;

        // Include the largest positive element if k is odd.
        if (k & 1) {
            product *= arr[right];
            right--;
            k--;
        }

        // Process remaining elements in pairs.
        k /= 2;

        for (int i = 0; i < k; i++) {

            int leftProduct = arr[left] * arr[left + 1];
            int rightProduct = arr[right] * arr[right - 1];

            // Choose the better pair.
            if (leftProduct > rightProduct) {
                product *= leftProduct;
                left += 2;
            } else {
                product *= rightProduct;
                right -= 2;
            }
        }

        // Return the maximum product.
        return product;
    }
};