#include <cstdio>
#include <iostream>
using namespace std;

int v[100010],a[200010],b[200010],w[200010];
int cnt=0;
bool k[100010];
int dis[100010];
int pre[100010];
int num[100010];
int ma;

void pr(int x){
	if(pre[x]!=-1) pr(pre[x]);
	if(x==ma){
		printf("%d",x);
    return;
	}
	else{
		printf("%d ",x);
		return;
	}
}

void add(int x,int y,int c){
	a[++cnt]=v[x];
	v[x]=cnt;
	b[cnt]=y;
	w[cnt]=c;
}

int main()
{
	int N,M,st,en;
	int ccc=0;
	int t1,t2,t3;
	scanf("%d %d %d %d",&N,&M,&st,&en);
	for(int i=1;i<=M;i++){
		scanf("%d %d %d",&t1,&t2,&t3);
		add(t1,t2,t3);
	}
	for(int i=1;i<=N;i++) dis[i]=1000000;
	t1=1000000;
	t2=0;
	dis[st]=0;
	pre[st]=-1;
	num[st]=1;
	for(int i=1;i<=N;i++){
		t1=1000000;
		for(int j=1;j<=N;j++){
			if(!k[j]&&t1>dis[j]){
				t1=dis[j];
        t2=j;
			}
		}
		k[t2]=true;
		for(int j=v[t2];j!=0;j=a[j]){
			if(!k[b[j]]&&t1+w[j]<dis[b[j]]){
				dis[b[j]]=t1+w[j];
				pre[b[j]]=t2;
				num[b[j]]=num[t2]+1;
			}
			else if(!k[b[j]]&&t1+w[j]==dis[b[j]]){
				if(num[b[j]]>num[t2]+1){
					num[b[j]]=num[t2]+1;
					pre[b[j]]=t2;
				}
			}
		}
	}
	ma=en;
	printf("%d\n",dis[en]);
	pr(en);
	return 0;
}

//class graph{
//    private:
//        int vSize,eSize;
//        struct edgeNode{
//            int weight;
//            int end;
//            edgeNode *next;
//            edgeNode(int e,int w,edgeNode *n=NULL) {end=e;weight=w;next=n;}
//        };
//        struct verNode{
//            int ver;
//            edgeNode *head;
//            verNode(edgeNode *h=NULL) {head=h;}
//        };
//        verNode *verList;
//    public:
//        graph(int size){
//            vSize=size;
//            eSize=0;
//            verList=new verNode[vSize+1];
//            for(int i=1;i<=vSize;i++) verList[i].ver=i;
//        }
//        ~graph(){
//            int i;
//            edgeNode *p;
//            for(i=1;i<=vSize;i++){
//                while((p=verList[i].head)!=NULL){
//                    verList[i].head=p->next;
//                    delete p;
//                }
//            }
//            delete [] verList;
//        }
//        void insert(int u,int v,int weight=1){
//            verList[u].head=new edgeNode(v,weight,verList[u].head);
//            eSize++;
//        }
//        void Dijkstra(int start,int end){
//          int *distance=new int[vSize+1];
//          int *prev=new int[vSize+1];
//          bool *known=new bool[vSize+1];
//          int u,min,i,j;
//          edgeNode *p;
//          for(int i=1;i<=vSize;i++){
//            distance[i]=100000;
//            known[i]=false;
//          }
//          distance[start]=0;
//          prev[start]=start;
//          for(i=2;i<=vSize;i++){
//            min=100000;
//            for(j=1;j<=vSize;j++){              //Ñ°ÕÒ×î¶Ì¾àÀë½áµã
//              if(!known[j] && distance[j]<min){
//                min=distance[j];
//                u=j;
//              }
//            }
//            known[u]=true;
//            for(p=verList[u].head;p!=NULL;p=p->next){
//              if(!known[p->end] && distance[p->end]>min+p->weight){
//                distance[p->end]=min+p->weight;
//                prev[p->end]=u;
//              }
//            }
//          }
//          printf("%d\n",distance[end]);
//          printpath(start,end,prev);
//        }
//        void printpath(int start,int end,int prev[]){
//          if(start==end){
//            printf("%d",verList[start].ver);
//            return;
//          }
//          printpath(start,prev[end],prev);
//          printf(" %d",verList[end].ver);
//        }
//};
//
//int main()
//{
//  int n,m,start,end;
//  int a,b,p;
//  scanf("%d %d %d %d",&n,&m,&start,&end);
//  graph g(n);
//  for(int i=0;i<m;i++){
//    scanf("%d %d %d",&a,&b,&p);
//    g.insert(a,b,p);
//  }
//  g.Dijkstra(start,end);
//  return 0;
//}
