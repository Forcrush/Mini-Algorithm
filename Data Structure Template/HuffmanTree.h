#ifndef HUFFMANTREE_H_INCLUDED
#define HUFFMANTREE_H_INCLUDED
#include <iostream>
#include <string>
using namespace std;

template<class T>
class HuffmanTree
{
    private:
        struct node{
            T data;
            int weight;
            int parent,left,right;
        };
        node *elem;
        int length;
    public:
        struct hfCode{
            T data;             //待编码字符
            string code;       //保存哈夫曼编码
        };
        HuffmanTree(const T *v,const int *w,int size){
            const int max=32767;
            int min1,min2;  //最小树、次小树权值
            int x,y;  //最小树、次小树下标
            length=2*size;
            elem=new node[length];
            for(int i=size;i<length;i++){
                elem[i].weight=w[i-size];
                elem[i].data=v[i-size];
                elem[i].parent=elem[i].left=elem[i].right=0;
            }
            //归并森林
            for(int i=size-1;i>0;i--){
                min1=min2=max;
                x=y=0;
                for(int j=i+1;j<length;++j){
                    if(elem[j].parent==0){
                        if(elem[j].weight<min1) {min2=min1;min1=elem[j].weight;x=y;y=j;}
                        else if(elem[j].weight<min2) {min2=elem[j].weight;x=j;}
                    }
                }
                elem[i].weight=min1+min2;
                elem[i].left=x;
                elem[i].right=y;
                elem[i].parent=0;
                elem[x].parent=i;
                elem[y].parent=i;
            }
        }
        void getCode(hfCode result[]){
            int size=length/2;
            int cur,par;
            for(int i=size;i<length;i++){
                result[i-size].data=elem[i].data;
                result[i-size].code="";
                par=elem[i].parent;
                cur=i;
                while(par){
                    if(elem[par].left==cur) result[i-size].code='0'+result[i-size].code;
                    else result[i-size].code='1'+result[i-size].code;
                    cur=par;
                    par=elem[par].parent;
                }
            }
        }
        ~HuffmanTree() {delete [] elem;}
};

//using example:
//int main()
//{
//    char ch[]={"aeistdn"};
//    int w[]={10,15,12,3,4,13,1};
//    HuffmanTree<char> tree(ch,w,7);
//    HuffmanTree<char>::hfCode result[7];
//    tree.getCode(result);
//    for(int i=0;i<7;i++) cout<<result[i].data<<' '<<result[i].code<<endl;
//    return 0;
//}

#endif // HUFFMANTREE_H_INCLUDED
