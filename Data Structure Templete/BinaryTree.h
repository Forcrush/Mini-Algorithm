#ifndef BINARYTREE_H_INCLUDED
#define BINARYTREE_H_INCLUDED
#include <iostream>
using namespace std;

template<class T>
class linkQueue{
    private:
        struct node{
            T data,value;
            node *next;
            node():next(NULL){}
            node(const T &x,node *N=NULL) {data=x;next=N;}
        };
        node *front,*rear;
    public:
        linkQueue() {front=rear=NULL;}
        ~linkQueue(){
            node *tmp;
            while(front!=NULL){
                tmp=front;
                front=front->next;
                delete tmp;
            }
        }
        bool isEmpty() {return front==NULL;}
        void enQueue(const T &x){
            if(rear==NULL) front=rear=new node(x);
            else {rear->next=new node(x);rear=rear->next;}
        }
        T deQueue(){
            node *tmp=front;
            T value=front->data;
            front=front->next;
            if(front==NULL) rear=NULL;
            delete tmp;
            return value;
        }
        T getHead() {return front->data;}
};

template<class T>
class BinaryTree
{
    private:
        struct Node{
            Node *left,*right,*parent;
            T data,value;
            Node():left(NULL),right(NULL),parent(NULL){}
            Node(T item,Node *L=NULL,Node *R=NULL,Node *P=NULL) {data=item;left=L;right=R;parent=P;}
            ~Node(){}
            void getvalue(T v) {value=v;}
        };
        Node *root;
        struct elem{
            Node *p;
            int num;
        };
    public:
        BinaryTree():root(NULL){}
        BinaryTree(const T &value) {root=new Node(value);}
        BinaryTree(const Node *p) {root=p;}
        ~BinaryTree() {clear();}
        T getRoot() const {return root->data;}
        T getLeft() const {return root->left->data;}
        T getRight() const {return root->right->data;}
        void makeTree(const T &x,BinaryTree &lt,BinaryTree &rt){
            root=new Node(x,lt.root,rt.root);
            lt.root=NULL;
            rt.root=NULL;
        }
        void delLeft(){
            BinaryTree tmp=root->left;
            root->left=NULL;
            tmp.clear();
        }
        void delRight(){
            BinaryTree tmp=root->right;
            root->right=NULL;
            tmp.clear();
        }
        bool isEmpty() const {return root==NULL;}
        void clear() {if(root!=NULL) clear(root); root=NULL;}
        int size() const {return size(root);}
        int height() const {return height(root);}
        void preOrder() const {if(root!=NULL) preOrder(root);} //cout<<"\n前序遍历:";
        void midOrder() const {if(root!=NULL) midOrder(root);} //cout<<"\n中序遍历:";
        void postOrder() const {if(root!=NULL) postOrder(root);}  //cout<<"\n后序遍历:";
        void levelOrder() const {if(root!=NULL) levelOrder(root);}  //cout<<"\n层级遍历:";
        bool isCompleteTree(){
            linkQueue<elem> que;
            elem cur,child;
            int count=1,last=1;
            if(root==NULL) return true;
            cur.p=root;
            cur.num=1;
            que.enQueue(cur);
            while(!que.isEmpty()){
                cur=que.deQueue();
                if(cur.p->left!=NULL){
                    ++count;
                    child.p=cur.p->left;
                    last=child.num=cur.num*2;
                    que.enQueue(child);
                }
                if(cur.p->right!=NULL){
                    ++count;
                    child.p=cur.p->right;
                    last=child.num=cur.num*2+1;
                    que.enQueue(child);
                }
            }
            return count==last;
        }
//        void creatTree(T flag){           //构造法1
//            linkQueue<Node * > que;
//            Node * tmp;
//            T x,ldata,rdata;
//            cout<<"\nInput root:";
//            cin>>x;
//            root=new Node(x);
//            //cout<<"root:"<<root->left<<endl;
//            que.enQueue(root);
//            cout<<"isEMpty?:"<<que.isEmpty()<<endl;  //检查是否放进去了
//            while(!que.isEmpty()){
//                tmp=que.deQueue();
//                cout<<"\nInput"<<tmp->data<<"'s son-Node:";
//                cin>>ldata>>rdata;
//                if(ldata!=flag) que.enQueue(tmp->left=new Node(ldata));
//                if(rdata!=flag) que.enQueue(tmp->right=new Node(rdata));
//            }
//        }
        void creatTree(){   //构造法3
            int leftdata,rightdata,valuedata,n,rootpos;
            cin>>n;
            Node *nodes=new Node[n+1];
            for(int i=1;i<=n;i++){
                cin>>leftdata>>rightdata>>valuedata;
                nodes[i].getvalue(valuedata);
                if(leftdata!=0){
                    nodes[i].left=&nodes[leftdata];
                    nodes[leftdata].parent=&nodes[i];
                }
                if(rightdata!=0){
                    nodes[i].right=&nodes[rightdata];
                    nodes[rightdata].parent=&nodes[i];
                }
            }
            for(int i=1;i<=n;i++){
                if(nodes[i].parent==NULL) {rootpos=i;break;} //-&nodes[1]+1
            }
            root=new Node(nodes[rootpos].value);
            linkQueue<Node * > nodeque1,nodeque2;
            Node *tmp1;
            Node *tmp2;
            Node *initial=new Node(rootpos);
            nodeque1.enQueue(initial);
            nodeque2.enQueue(root);
            while(!nodeque1.isEmpty()){
                tmp1=nodeque1.deQueue();
                tmp2=nodeque2.deQueue();
                int nodenum=tmp1->data;
                if(nodes[nodenum].left!=0){
                    nodeque1.enQueue(tmp1->left=new Node(nodes[nodenum].left-&nodes[1]+1));
                    nodeque2.enQueue(tmp2->left=new Node(nodes[nodes[nodenum].left-&nodes[1]+1].value));
                }
                if(nodes[nodenum].right!=0){
                    nodeque1.enQueue(tmp1->right=new Node(nodes[nodenum].right-&nodes[1]+1));
                    nodeque2.enQueue(tmp2->right=new Node(nodes[nodes[nodenum].right-&nodes[1]+1].value));
                }
            }
        }
    private:
        int height(Node *t) const{
            if(t==NULL) return 0;
            else{
                int lt=height(t->left),rt=height(t->right);
                return 1+((lt>rt)?lt:rt);
            }
        }
        void clear(Node *t){
            if(t->left!=NULL) clear(t->left);
            if(t->right!=NULL) clear(t->right);
            delete t;
        }
        int size(Node *t) const {if(t==NULL) return 0; return 1+size(t->left)+size(t->right);}
        void preOrder(Node *t) const{
            if(t!=NULL){
                cout<<t->data<<' ';
                preOrder(t->left);
                preOrder(t->right);
            }
        }
        void midOrder(Node *t) const{
            if(t!=NULL){
                midOrder(t->left);
                cout<<t->data<<' ';
                midOrder(t->right);
            }
        }
        void postOrder(Node *t) const{
            if(t!=NULL){
                postOrder(t->left);
                postOrder(t->right);
                cout<<t->data<<' ';
            }
        }
        void levelOrder(Node *t) const{
            linkQueue<Node *> que;
            Node *cur;
            if(t==NULL) return;
            que.enQueue(root);
            while(!que.isEmpty()){
                cur=que.deQueue();
                if(cur->left!=NULL) que.enQueue(cur->left);
                if(cur->right!=NULL) que.enQueue(cur->right);
                cout<<cur->data<<' ';
            }
            cout<<endl;
        }
};

#endif // BINARYTREE_H_INCLUDED
