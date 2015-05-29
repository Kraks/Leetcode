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
    vector<int> preorderTraversal(TreeNode *root) {
    	std::vector<int> v;
    	return this->auxPreorderTraversal(root, v);
    }

    vector<int>& auxPreorderTraversal(TreeNode* root, vector<int>& res) {
    	if (root == NULL) return res;
        res.push_back(root->val);
    	if (root->left != NULL) {
    		this->auxPreorderTraversal(root->left, res);
    	}
    	if (root->right != NULL) {
    		this->auxPreorderTraversal(root->right, res);
    	}
    	return res;
    }
};