#ifndef ADJLISTGRAPH_H_INCLUDED
#define ADJLISTGRAPH_H_INCLUDED

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

template<class TypeOfVer,class TypeOfEdge>
class adjListGragh{
    private:
        int Vers,Edges;
        struct edgeNode{ //����ߵĽ����
            int end;
            TypeOfEdge weight;
            edgeNode *next;
            edgeNode(int e,TypeOfEdge w,edgeNode *n=NULL) {end=e;weight=w;next=n;}
        };
        struct verNode{ //���涥��Ľ����
            TypeOfVer ver;
            edgeNode *head;
            verNode(edgeNode *h=NULL) {head=h;}
        };
        struct EulerNode{   //����ŷ����·�Ľ����
            int NodeNum;
            EulerNode *next;
            EulerNode(int ver) {NodeNum=ver;next=NULL;}
        };
        verNode *verList; //�ڽ�������Ψһ�����ݳ�Ա
        void dfs(int start,bool visited[]) const{
            edgeNode *p=verList[start].head;
            cout<<verList[start].ver<<' ';
            visited[start]=true;
            while(p!=NULL){
                if(visited[p->end]==false) dfs(p->end,visited);
                p=p->next;
            }
        }
        EulerNode *EulerCircuit(int start,EulerNode *&end){
            EulerNode *beg;
            int nextNode;
            beg=end=new EulerNode(start);
            while(verList[start].head!=NULL){
                nextNode=verList[start].head->end;
                remove(start,nextNode);
                remove(nextNode,start);
                start=nextNode;
                end->next=new EulerNode(start);
                end=end->next;
            }
            return beg;
        }
        verNode *clone() const{
            verNode *tmp=new verNode[Vers];
            edgeNode *p;
            for(int i=0;i<Vers;i++){
                tmp[i].ver=verList[i].ver;
                p=verList[i].head;
                while(p!=NULL){
                    tmp[i].head=new edgeNode(p->end,p->weight,tmp[i].head);
                    p=p->next;
                }
            }
            return tmp;
        }
    public:
        adjListGragh(int vsize,const TypeOfVer d[]){
            Vers=vsize;
            Edges=0;
            verList=new verNode[vsize];
            for(int i=0;i<Vers;i++) verList[i].ver=d[i];
        }
        ~adjListGragh(){
            int i;
            edgeNode *p;
            for(int i=0;i<Vers;i++){
                while((p=verList[i].head)!=NULL){
                    verList[i].head=p->next;
                    delete p;
                }
            }
            delete [] verList;
        }
        bool insert(int u,int v,TypeOfEdge w){
            verList[u].head=new edgeNode(v,w,verList[u].head);
            Edges++;
            return true;
        }
        bool remove(int u,int v){
            edgeNode *p=verList[u].head,*q;
            if(p==NULL) return false;
            if(p->end==v){
                verList[u].head=p->next;
                delete p;
                Edges--;
                return true;
            }
            while(p->next!=NULL && p->next->end!=v) p=p->next;
            if(p->next==NULL) return false;
            q=p->next;
            p->next=q->next;
            delete q;
            Edges--;
            return true;
        }
        bool exist(int u,int v) const{
            edgeNode *p=verList[u].head;
            while(p!=NULL && p->end!=v) p=p->next;
            if(p==NULL) return false;
            else return true;
        }
        void dfs() const{ //�����������
            bool *visited=new bool[Vers];
            for(int i=0;i<Vers;i++) visited[i]=false;
            cout<<"��ǰͼ��dfs����:"<<endl;
            for(int i=0;i<Vers;i++){
                if(visited[i]==true) continue;
                dfs(i,visited);
                cout<<endl; //ÿһ�б�ʾһ��������
            }
        }
        void bfs() const{ //�����������
            bool *visited=new bool[Vers];
            int currentNode;
            linkQueue<int> q;
            edgeNode *p;
            for(int i=0;i<Vers;i++) visited[i]=false;
            cout<<"��ǰͼ��bfs����:"<<endl;
            for(int i=0;i<Vers;i++){
                if(visited[i]==true) continue;
                q.enQueue(i);
                while(!q.isEmpty()){
                    currentNode=q.deQueue();
                    if(visited[currentNode]==true) continue;
                    cout<<verList[currentNode].ver<<' ';
                    visited[currentNode]=true;
                    p=verList[currentNode].head;
                    while(p!=NULL){
                        if(visited[p->end]==false) q.enQueue(p->end);
                        p=p->next;
                    }
                }
            cout<<endl; //ÿһ�б�ʾһ��������
            }
        }
        void EulerCircuit(TypeOfVer start){ //Ѱ��ŷ����·
            EulerNode *beg,*end,*p,*q,*tb,*te;  //beg,endΪŷ����·�������յ�
            int numofdegree;
            edgeNode *r;
            verNode *tmp;
            //����Ƿ����ŷ����·
            if(Edges==0) {cout<<"NO EulerCircuit"<<endl;return;}
            for(int i=0;i<Vers;i++){
                numofdegree=0;
                r=verList[i].head;
                while(r!=0) {numofdegree++;r=r->next;}
                if(numofdegree==0 || numofdegree%2) {cout<<"NO EulerCircuit"<<endl;return;}
            }
            //Ѱ����ʼ�����
            int i;
            for(i=0;i<Vers;i++)
                if(verList[i].ver==start) break;
            if(i==Vers) {cout<<"NO start-point"<<endl;return;}

            tmp=clone();
            //Ѱ�Ҵ�i������·���������յ�Ϊbeg��end
            beg=EulerCircuit(i,end);
            while(true){
                p=beg;
                while(p->next!=NULL){ //����Ƿ��б���δ����
                    if(verList[p->next->NodeNum].head!=NULL) break;
                    else p=p->next;
                }
                if(p->next==NULL) break; //���б߶��ѷ���
                q=p->next;  //����δ�����ʱߵĽ��
                tb=EulerCircuit(q->NodeNum,te);  //�Ӵ˽�㿪ʼdfs
                te->next=q->next;   //����������·��ƴ�ӵ�ԭ·����
                p->next=tb;
                delete q;
            }
            //�ָ�ԭͼ
            delete [] verList;
            verList=tmp;
            cout<<"EulerCircuit:"<<endl;
            while(beg!=NULL){
                cout<<verList[beg->NodeNum].ver<<' ';
                p=beg;beg=beg->next;
                delete p;
            }
        }
        void topSort() const{ //Ѱ����������
            linkQueue<int> q;
            edgeNode *p;
            int current;
            int *indegree=new int[Vers];
            for(int i=0;i<Vers;i++) indegree[i]=0;
            for(int i=0;i<Vers;i++){
                for(p=verList[i].head;p!=NULL;p=p->next) ++indegree[p->end];
            }
            for(int i=0;i<Vers;i++)
                if(indegree[i]==0) q.enQueue(i);
            cout<<"Topsort:"<<endl;
            while(!q.isEmpty()){
                current=q.deQueue();
                cout<<verList[current].ver<<' ';
                for(p=verList[current].head;p!=NULL;p=p->next)
                    if(--indegree[p->end]==0) q.enQueue(p->end);
            }
            cout<<endl;
        }
};

#endif // ADJLISTGRAPH_H_INCLUDED
