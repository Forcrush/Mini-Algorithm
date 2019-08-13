#include <cstdio>
using namespace std;

int begin=1,tail=0,Q[100001]={0};
int begin_=1,tail_=0,Q_[100001]={0};
int tmp=0,de; //de为出队元素

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
        int topSort(){
            int *inDegrees=new int[vSize+1];
            for(int i=1;i<=vSize;++i) inDegrees[i]=0;
            for(int i=1;i<=vSize;++i){
                edgeNode *p=verList[i].head;
                while(p!=NULL){
                    ++inDegrees[p->end];
                    p=p->next;
                }
            }
            bool *visited=new bool[vSize+1];
            for(int j=1;j<=vSize;++j) visited[j]=false;
            for(int i=1;i<=vSize;++i){
                if(inDegrees[i]==0) Q[++tail]=i;
            }
            while(begin<=tail){
                if(begin<=tail) ++tmp;
                while(begin<=tail){
                    de=Q[begin];
                    begin++;
                    visited[de]=true;
                    edgeNode *p=verList[de].head;
                    while(p!=NULL){
                        if(visited[p->end]==false)
                            if(--inDegrees[p->end]==0) Q_[++tail_]=p->end;
                        p=p->next;
                    }
                }
                if(begin_<=tail_) tmp++;
                while(begin_<=tail_){
                    de=Q_[begin_];
                    begin_++;
                    visited[de]=true;
                    edgeNode *p=verList[de].head;
                    while(p!=NULL){
                        if(visited[p->end]==false)
                           if(--inDegrees[p->end]==0) Q[++tail]=p->end;
                        p=p->next;
                    }
                }
            }
            return tmp;
        }
};

int main()
{
    int n,m,u,v;
    scanf("%d %d",&n,&m);
    graph g(n);
    for(int i=0;i<m;++i){
        scanf("%d %d",&u,&v);
        g.insert(u,v);
    }
    printf("%d",g.topSort());
    return 0;
}
