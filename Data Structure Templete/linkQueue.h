#ifndef LINKQUEUE_H_INCLUDED
#define LINKQUEUE_H_INCLUDED

template<class T>
class linkQueue{
    private:
        struct node{
            T data;
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

#endif // LINKQUEUE_H_INCLUDED
