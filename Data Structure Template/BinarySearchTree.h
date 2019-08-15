#ifndef BINARYSEARCHTREE_H_INCLUDED
#define BINARYSEARCHTREE_H_INCLUDED
#include <iostream>
using namespace std;

template<class T>
class BinarySearchTree{
    private:
        struct bsnode{
            T data;
            bsnode *left,*right;
            bsnode(const T &x,bsnode *l,bsnode *r):data(x),left(l),right(r) {}
        };
        bsnode *root;
    public:
        BinarySearchTree() {root=NULL;}
        ~BinarySearchTree() {makeEmpty(root);}
        bool isEmpty() {return root==NULL;}
        bool find(const T &x) const {return find(x,root);}
        void insert(const T &x) {insert(x,root);}
        void remove(const T &x) {remove(x,root);}
        void delete_less_than(const T x) {delete_less_than(x,root);}
        void delete_greater_than(const T x) {delete_greater_than(x,root);}
        void delete_interval(T x,T y) {if(x<=y) delete_interval(x,y,root);}
        bool find_ith(const T&i)  {return find_ith(i,root);}
        int pointsize(bsnode *t){   //结点规模
            if(t == NULL) return 0;
            else return (pointsize(t->left) + pointsize(t->right) + 1);
        }
    private:
        void makeEmpty(bsnode * &t) {
            if(t == NULL) return;
            if(t->left != NULL) makeEmpty(t->left);
            if(t->right != NULL) makeEmpty(t->right);
            delete t;
        }
        bool find(const T &x,bsnode *t) const{
            if(t==NULL) return false;
            else if(x<t->data) return find(x,t->left);
            else if(x>t->data) return find(x,t->right);
            else return true;
        }
        void insert(const T &x,bsnode * &t){   //注意使用了指针引用 联系子父结点
            if(t==NULL) t=new bsnode(x,NULL,NULL);
            else if(x<=t->data) insert(x,t->left);  //使其可储存重复元素
            else if(x>t->data) insert(x,t->right);
        }
        void remove(const T &x,bsnode * &t){   //注意使用了指针引用 联系子父结点
            if(t==NULL) return;
            if(x<t->data) remove(x,t->left);
            else if(x>t->data) remove(x,t->right);
            else if(t->left!=NULL && t->right!=NULL){   //有两个儿子
                bsnode *tmp=t->right;
                while(tmp->left!=NULL) tmp=tmp->left;
                t->data=tmp->data;
                remove(t->data,t->right);
            }
            else{
                bsnode *oldnode=t;
                t=(t->left!=NULL)?t->left:t->right;
                delete oldnode;
            }
        }
        void delete_less_than(const T &x,bsnode * &t){
            if(t==NULL) return;
            if(t->data==x){
                makeEmpty(t->left);
                t->left==NULL;
                return;
            }
            else if(t->data<x){
                bsnode *tmp=t;
                t=t->right;
                delete tmp;
                delete_less_than(x,t);
            }
            else delete_less_than(x,t->left);
        }
        void delete_greater_than(const T &x,bsnode * &t){
            if(t==NULL) return;
            if(t->data==x){
                makeEmpty(t->right);
                t->right==NULL;
                return;
            }
            else if(t->data>x){
                bsnode *tmp=t;
                t=t->left;
                delete tmp;
                delete_greater_than(x,t);
            }
            else delete_greater_than(x,t->right);
        }
        void delete_interval(const T x,const T y,bsnode * &t){
            if(t==NULL) return;
            if(t->data<=x) delete_interval(x,y,t->right);
            else if(t->data>=y) delete_interval(x,y,t->left);
            else{
                delete_greater_than(x,t->left);
                delete_less_than(y,t->right);
                remove(t->data,t);
            }
        }
        bool find_ith(const T&i,bsnode *&t){
            if(t==NULL) return false;
            int lfsize=pointsize(t->left);
            if(i<=lfsize) return find_ith(i,t->left);
            else if(i==lfsize+1) {cout<<t->data<<'\n';return true;}
            else return find_ith(i-lfsize-1,t->right);
        }
};

#endif // BINARYSEARCHTREE_H_INCLUDED
