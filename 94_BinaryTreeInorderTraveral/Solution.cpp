/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode *root) {
    	std::vector<int> v;
    	return this->auxInorderTraversal(root, v);
    }

    vector<int>& auxInorderTraversal(TreeNode* root, vector<int>& res) {
    	if (root == NULL) return res;
    	if (root->left != NULL) {
    		this->auxInorderTraversal(root->left, res);
    	}
    	res.push_back(root->val);
    	if (root->right != NULL) {
    		this->auxInorderTraversal(root->right, res);
    	}
    	return res;
    }
};