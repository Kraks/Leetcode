/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  struct TreeLinkNode *left, *right, *next;
 * };
 *
 */

typedef struct TreeLinkNode TreeLinkNode;

void auxConnect(TreeLinkNode* node){
    if (node->left) auxConnectLeft(node->left, node);
    if (node->right) auxConnectRight(node->right, node);
}

void auxConnectLeft(TreeLinkNode* node, TreeLinkNode* parent) {
    node->next = parent->right;
    auxConnect(node);
}

void auxConnectRight(TreeLinkNode* node, TreeLinkNode* parent) {
    if (parent->next){
        node->next = parent->next->left;
    }
    else {
        node->next = NULL;
    }
    auxConnect(node);
}
 
void connect(struct TreeLinkNode *root) {
    if (root) {
        root->next = NULL;
        if (root->left) auxConnectLeft(root->left, root);
        if (root->right) auxConnectRight(root->right, root);
    }
}
