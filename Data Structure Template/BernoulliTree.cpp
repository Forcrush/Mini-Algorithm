#ifndef MINBINARYHEAP_H_INCLUDED
#define MINBINARYHEAP_H_INCLUDED
#include <iostream>
#include <string.h>
using namespace std;

template<class T>
class MinBinaryHeap{
    private:
        int currentsize;
        T *array;
        int maxsize;
        void doublespace(){
            T *tmp=array;
            maxsize*=2;
            array=new T[maxsize];
            for(int i=0;i<=currentsize;++i) array[i]=tmp[i];
            delete [] tmp;
        }
        void buildHeap(){
            for(int i=currentsize/2;i>0;i--) percolateDown(i);
        }
        void percolateDown(int hole){
            int child;
            T tmp=array[hole];
            for(;hole*2<=currentsize;hole=child){
                child=hole*2;
                if(child!=currentsize&&array[child+1]<array[child]) child++;
                if(array[child]<tmp) array[hole]=array[child];
                else break;
            }
            array[hole]=tmp;
        }
    public:
        MinBinaryHeap(int capacity=100) {array=new T[capacity];maxsize=capacity;currentsize=0;}
        MinBinaryHeap(const T data[],int size):maxsize(size+10),currentsize(size){
            array=new T[maxsize];
            for(int i=0;i<size;i++) array[i+1]=data[i];
            buildHeap();
        }
        ~MinBinaryHeap() {delete [] array;}
        bool isEmpty() const {return currentsize==0;}
        void enQueue(const T &x){
            if(currentsize==maxsize-1) doublespace();
            //ÏòÉÏ¹ýÂË
            int hole=++currentsize;
            for(;hole>1&&x<array[hole/2];hole/=2) array[hole]=array[hole/2];
            array[hole]=x;
        }
        T deQueue(){
            T minitem;
            minitem=array[1];
            array[1]=array[currentsize--];
            percolateDown(1);
            return minitem;
        }
        T getHead() {return array[1];}
        void output() {for(int i=1;i<=currentsize;i++) cout<<array[i];}
};

#endif // MINBINARYHEAP_H_INCLUDED

int main()
{
    MinBinaryHeap<int> t;
    string s;
    struct Op{
        int type;
        int data;
    };
    int num,times;
    cin>>times;
    Op op[times];
    for(int i=0;i<times;++i){
        cin>>s;
        if(s=="insert") {cin>>num;op[i].type=1;op[i].data=num;}
        if(s=="delete") op[i].type=2;
        if(s=="min") op[i].type=3;
    }
    for(int i=0;i<times;++i){
        if(op[i].type==1) t.enQueue(op[i].data);
        if(op[i].type==2) t.deQueue();
        if(op[i].type==3) cout<<t.getHead()<<endl;
    }
    return 0;
}
