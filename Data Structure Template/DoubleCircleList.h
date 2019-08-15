#ifndef DOUBLECIRCLELIST_H_INCLUDED
#define DOUBLECIRCLELIST_H_INCLUDED


template <class T>
class DoubleCircleList{
    private:
        struct node{
            T data;
            node *prev,*next;
            node() {prev=NULL;next=NULL;}
            node(const T &x,node *p=NULL,node *n=NULL) {data=x;prev=p;next=n;}
            ~node() {}
        };
        node *head;
        int size;
    public:
        DoubleCircleList():head(NULL),size(0){}
        ~DoubleCircleList(){
            node *p=head,*q;
            while(p!=head){
                q=p->next;
                delete p;
                size--;
                p=q;
            }
        }
        int length() {return size;}
    class MyItr{
        friend class DoubleCircleList;
        private:
            node *cur;
        public:
            MyItr(node *p=NULL):cur(p){}
            T &operator*() {return cur->data;} //返回迭代器指向元素
            MyItr operator++(int x){               //后缀++
                MyItr tmp=*this;
                cur=cur->next;
                return tmp;
            }
            MyItr operator++() {return cur=cur->next;}        //前缀++
            MyItr operator--(int x){               //后缀--
                MyItr tmp=*this;
                cur=cur->prev;
                return tmp;
            }
            MyItr operator--() {return cur=cur->prev;}       //前缀--
            bool operator==(const MyItr &a) {return cur==a.cur;}  //判断迭代器相等
            bool operator!=(const MyItr &a) {return cur!=a.cur;}   //判断迭代器不等
            bool isNULL() {return cur==NULL;}  //判断迭代器指向对象是否为空
    };
    MyItr begin() const {return head;}
    void insert(MyItr &p,const T &a){
        if(p.cur==NULL){
            head=p.cur=new node(a);
            head->prev=head;
            head->next=head;
        }
        else{
            p.cur->next=p.cur->next->prev=new node(a,p.cur,p.cur->next);
            p.cur=p.cur->next;
        }
        size++;
    }
    void erase(MyItr &p){
        if(p.cur==NULL) return;         //空表
        if(p.cur->next==p.cur) {delete p.cur;head=p.cur=NULL;}  //只有一个元素
        else{
            node *q;
            q=p.cur;
            q->next->prev=q->prev;
            q->prev->next=q->next;
            p.cur=q->next;
            if(q==head) head=q->next;
            delete q;
        }
        size--;
    }
    MyItr search(const T &a){
        node *p=head;
        if(p==NULL) return NULL;
        do{
            if(a==p->data) return p;
            p=p->next;
        } while(p!=head);
        return NULL;
    }
};
#endif // DOUBLECIRCLELIST_H_INCLUDED
