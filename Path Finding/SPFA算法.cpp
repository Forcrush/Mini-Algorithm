#include <cstdio>
#include <iostream>
using namespace std;

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

class graph{
    private:
        int vSize,eSize;
        struct edgeNode{
            int weight;
            int end;
            edgeNode *next;
            edgeNode(int e,int w,edgeNode *n=NULL) {end=e;weight=w;next=n;}
        };
        struct verNode{
            int ver;
            edgeNode *head;
            verNode(edgeNode *h=NULL) {head=h;}
        };
        verNode *verList;
    public:
        graph(int size){
            vSize=size;
            eSize=0;
            verList=new verNode[vSize+1];
            for(int i=1;i<=vSize;i++) verList[i].ver=i;
        }
        ~graph(){
            int i;
            edgeNode *p;
            for(i=1;i<=vSize;i++){
                while((p=verList[i].head)!=NULL){
                    verList[i].head=p->next;
                    delete p;
                }
            }
            delete [] verList;
        }
        void insert(int u,int v,int weight=1){
            verList[u].head=new edgeNode(v,weight,verList[u].head);
            eSize++;
        }
        void spfa(int start,int end){
          int *distance=new int[vSize+1];
          int *prev=new int[vSize+1];
          int v;
          edgeNode *p;
          linkQueue<int> q;
          for(int i=1;i<=vSize;i++) distance[i]=100000;
          distance[start]=0;
          prev[start]=start;
          q.enQueue(start);
          while(!q.isEmpty()){
            v=q.deQueue();
            for(p=verList[v].head;p!=NULL;p=p->next){
              if(distance[v]+p->weight<distance[p->end]){
                distance[p->end]=distance[v]+p->weight;
                prev[p->end]=v;
                q.enQueue(p->end);
              }
            }
          }
          printf("%d",distance[end]);
//          for(int i=1;i<=vSize;i++){
//            cout<<"from"<<start<<"to"<<verList[i].ver<<":"<<endl;
//            printpath(start,i,prev);
//            cout<<"length:"<<distance[i]<<endl;
//          }
        }
        void printpath(int start,int end,int prev[]){
          if(start==end){
            cout<<verList[start].ver;
            return;
          }
          printpath(start,prev[end],prev);
          cout<<"-"<<verList[end].ver;
        }
};

int main()
{
  int n,m,start,end;
  int a,b,p;
  scanf("%d %d %d %d",&n,&m,&start,&end);
  graph g(n);
  for(int i=0;i<m;i++){
    scanf("%d %d %d",&a,&b,&p);
    g.insert(a,b,p);
  }
  g.spfa(start,end);
  return 0;
}
