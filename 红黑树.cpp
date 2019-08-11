#include <iostream>
#include <algorithm>

using namespace std;

enum { red = 0, black = 1 };

struct Node
{
    int key;
    bool color;
    Node* parent;
    Node* left;
    Node* right;
    Node(int key = 0)
    {
        this->key = key;
        this->color = red;
        this->parent = this->left = this->right = nullptr;
    }
};

class RBTree
{
private:
    Node* root;

private:
    void rotate_left(Node* x);
    void rotate_right(Node* x);
    void destroy(Node* node);
    void insert_rebalance(Node* x);
    void erase_rebalance(Node* z);
    void in_order(Node* node);

public:
    RBTree();
    ~RBTree();
    Node* insert(int key);
    Node* find(int key);
    void erase(int key);
    void print();
};

RBTree::RBTree()
{
    root = nullptr;
}

void RBTree::destroy(Node* node)
{
    if (node == nullptr)
        return;

    destroy(node->left);
    destroy(node->right);
    delete node;
}

RBTree::~RBTree()
{
    destroy(root);
    root = nullptr;
}

void RBTree::rotate_left(Node* x)
{
    Node* y = x->right;

    x->right = y->left;
    if (y->left)
        y->left->parent = x;
    y->parent = x->parent;

    if (x == root)
        root = y;
    else if (x == x->parent->left)
        x->parent->left = y;
    else
        x->parent->right = y;

    y->left = x;
    x->parent = y;
}

void RBTree::rotate_right(Node* x)
{
    Node* y = x->left;

    x->left = y->right;
    if (y->right)
        y->right->parent = x;
    y->parent = x->parent;

    if (x == root)
        root = y;
    else if (x == x->parent->right)
        x->parent->right = y;
    else
        x->parent->left = y;

    y->right = x;
    x->parent = y;
}

Node* RBTree::find(int key)
{
    Node* z = root;

    while (z)
    {
        if (key < z->key)
            z = z->left;
        else if (key > z->key)
            z = z->right;
        else
            return z;
    }

    return z;
}

void RBTree::insert_rebalance(Node* x)
{
    x->color = red;

    while (x != root && x->parent->color == red)
    {
        if (x->parent == x->parent->parent->left)
        {
            Node* y = x->parent->parent->right;

            if (y && y->color == red)           /* Case 1 */
            {
                x->parent->color = black;
                y->color = black;
                x->parent->parent->color = red;
                x = x->parent->parent;
            }
            else
            {
                if (x == x->parent->right)      /* Case 2 */
                {
                    x = x->parent;
                    rotate_left(x);
                }

                x->parent->color = black;       /* Case 3 */
                x->parent->parent->color = red;
                rotate_right(x->parent->parent);
                break;
            }
        }
        else  /* left <-> right */
        {
            Node* y = x->parent->parent->left;

            if (y && y->color == red)
            {
                x->parent->color = black;
                y->color = black;
                x->parent->parent->color = red;
                x = x->parent->parent;
            }
            else
            {
                if (x == x->parent->left)
                {
                    x = x->parent;
                    rotate_right(x);
                }

                x->parent->color = black;
                x->parent->parent->color = red;
                rotate_left(x->parent->parent);
                break;
            }
        }
    }

    root->color = black;
}

Node* RBTree::insert(int key)
{
    if (root == nullptr)
    {
        root = new Node(key);
        root->color = black;
        return root;
    }

    Node* cur = root;
    Node* pre = nullptr;

    while (cur)
    {
        pre = cur;
        if (key < cur->key)
            cur = cur->left;
        else if (key > cur->key)
            cur = cur->right;
        else
            return nullptr; /* 不可重复插入 */
    }

    cur = new Node(key);
    cur->parent = pre;

    if (key < pre->key)
        pre->left = cur;
    else
        pre->right = cur;

    insert_rebalance(cur);

    return cur;
}

void RBTree::erase_rebalance(Node* z)
{
    Node* y = z;
    Node* x = nullptr;
    Node* x_parent = nullptr;

    if (y->left == nullptr)
        x = y->right;
    else if (y->right == nullptr)
        x = y->left;
    else /* 结点 z 的孩子都存在 */
    {
        y = y->right;
        while (y->left)
            y = y->left; /* 找到后继结点 */

        x = y->right;
    }

    /* y != z 说明结点 z 的孩子都存在 */
    if (y != z)
    {
        z->left->parent = y;
        y->left = z->left;

        if (y != z->right)
        {
            x_parent = y->parent;
            if (x)
                x->parent = y->parent;
            y->parent->left = x;
            y->right = z->right;
            z->right->parent = y;
        }
        else
            x_parent = y;

        if (root == z)
            root = y;
        else if (z->parent->left == z)
            z->parent->left = y;
        else
            z->parent->right = y;

        y->parent = z->parent;
        swap(y->color, z->color);
        y = z;
    }
    else
    {
        x_parent = y->parent;
        if (x)
            x->parent = y->parent;

        if (root == z)
            root = x;
        else if (z->parent->left == z)
            z->parent->left = x;
        else
            z->parent->right = x;
    }
    
    /* 
    经过上边的处理，y 指向真正要删除的结点（即文中所定义的 “原先结点”）；x 为 y 的左孩子
    或右孩子（也可能为空），作为结点 y 被删除后的替补结点（即文中所定义的 “当前结点”）。
    */

    if (y->color == black)
    {
        if (x != root && (x == nullptr || x->color == black))
        {
            if (x == x_parent->left)
            {
                Node* w = x_parent->right;

                if (w->color == red)                                     /* Case 1 */
                {
                    w->color = black;
                    x_parent->color = red;
                    rotate_left(x_parent);
                    w = x_parent->right;
                }

                if ((w->left == nullptr || w->left->color == black) &&   /* Case 2 */
                    (w->right == nullptr || w->right->color == black))
                {
                    w->color = red;
                    x = x_parent;
                    x_parent = x_parent->parent;
                }
                else
                {
                    if (w->right == nullptr || w->right->color == black) /* Case 3 */
                    {
                        if (w->left)
                            w->left->color = black;
                        w->color = red;
                        rotate_right(w);
                        w = x_parent->right;
                    }

                    w->color = x_parent->color;                          /* Case 4 */
                    x_parent->color = black;
                    if (w->right)
                        w->right->color = black;
                    rotate_left(x_parent);
                }
            }
            else  /* left <-> right */
            {
                Node* w = x_parent->left;

                if (w->color == red)
                {
                    w->color = black;
                    x_parent->color = red;
                    rotate_right(x_parent);
                    w = x_parent->left;
                }

                if ((w->right == nullptr || w->right->color == black) &&
                    (w->left == nullptr || w->left->color == black))
                {
                    w->color = red;
                    x = x_parent;
                    x_parent = x_parent->parent;
                }
                else
                {
                    if (w->left == nullptr || w->left->color == black)
                    {
                        if (w->right)
                            w->right->color = black;
                        w->color = red;
                        rotate_left(w);
                        w = x_parent->left;
                    }

                    w->color = x_parent->color;
                    x_parent->color = black;
                    if (w->left)
                        w->left->color = black;
                    rotate_right(x_parent);
                }
            }
        }

        if (x)
            x->color = black;
    }
}

void RBTree::erase(int key)
{
    Node* z = find(key);

    if (z)
    {
        erase_rebalance(z);
        delete z;
    }
}

void RBTree::in_order(Node* node)
{
    if (node == nullptr)
        return;

    in_order(node->left);
    cout << "( " << node->key << ", " << node->color << " )" << endl;
    in_order(node->right);
}

void RBTree::print()
{
    in_order(root);
    cout << endl;
}

int main()
{
    cout << "red: " << red << ", black: " << black << endl << endl;

    RBTree rb_tree;

    /* test "insert" */
    rb_tree.insert(7);
    rb_tree.insert(2);
    rb_tree.insert(1); rb_tree.insert(1);
    rb_tree.insert(5);
    rb_tree.insert(3);
    rb_tree.insert(6);
    rb_tree.insert(4);
    rb_tree.insert(9);
    rb_tree.insert(8);
    rb_tree.insert(11); rb_tree.insert(11);
    rb_tree.insert(10);
    rb_tree.insert(12);
    rb_tree.print();

    /* test "find" */
    Node* p = nullptr;
    cout << ((p = rb_tree.find(2)) ? p->key : -1) << endl;
    cout << ((p = rb_tree.find(100)) ? p->key : -1) << endl << endl;

    /* test "erase" */
    rb_tree.erase(1);
    rb_tree.print();
    rb_tree.erase(9);
    rb_tree.print();
    rb_tree.erase(11);
    rb_tree.print();

    return 0;
}

