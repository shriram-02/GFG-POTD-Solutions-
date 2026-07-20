class Solution {
    class TrieNode {
        TrieNode[] child = new TrieNode[26];
        int freq = 0;
    }

    public ArrayList<String> findPrefixes(ArrayList<String> arr) {
        TrieNode root = new TrieNode();

        for (String word : arr) {
            TrieNode curr = root;
            for (char ch : word.toCharArray()) {
                int idx = ch - 'a';
                if (curr.child[idx] == null)
                    curr.child[idx] = new TrieNode();
                curr = curr.child[idx];
                curr.freq++;
            }
        }

        ArrayList<String> ans = new ArrayList<>();

        for (String word : arr) {
            TrieNode curr = root;
            StringBuilder sb = new StringBuilder();
            for (char ch : word.toCharArray()) {
                curr = curr.child[ch - 'a'];
                sb.append(ch);
                if (curr.freq == 1)
                    break;
            }
            ans.add(sb.toString());
        }

        return ans;
    }
}