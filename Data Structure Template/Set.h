#ifndef SET_H_INCLUDED
#define SET_H_INCLUDED
#include <iostream>
using namespace std;

template<class T>
class set
{
    friend set<T> operator*(const set<T> &a,const set<T> &b){
        set<T> c;
        for(int i=0;i<a.size;i++) if(b.exist(a.elem[i])) c.insert(a.elem[i]);
        return c;
    }
    friend set<T> operator+(const set<T> &a,const set<T> &b){
        set<T> c=a;
        for(int i=0;i<b.size;i++) c.insert(b.elem[i]);
        return c;
    }
    friend set<T> operator-(const set<T> &a,const set<T> &b){
        set<T> c;
        for(int i=0;i<a.size;i++) if(!b.exist(a.elem[i])) c.insert(a.elem[i]);
        return c;
    }
    private:
        T *elem;
        int size,volume;
        void doublespace(){
            volume*=2;
            T *tmp=new T[volume];
            for(int i=0;i<size;i++) tmp[i]=elem[i];
            delete [] elem;
            elem=tmp;
        }
        bool exist(T x) const{
            for(int i=0;i<size;i++) if(elem[i]==x) return true;
            return false;
        }
    public:
        set(){size=0;volume=20;elem=new T[volume];}
        set(const set<T> &a){
            size=a.size;
            volume=a.volume;
            elem=new T[volume];
            for(int i=0;i<size;i++) elem[i]=a.elem[i];
        }
        ~set() {delete [] elem;}
        int getsize() {return size;}
        bool isEmpty() {return size==0;}
        void insert(T x){
            if(!exist(x)){
                if(size==volume) doublespace();
                elem[size++]=x;
            }
        }
        void erase(T x){
            bool flag=false;
            int i;
            for(i=0;i<size;i++){
                if(elem[i]==x) {flag=true;break;}
            }
            if(!flag) cout<<"Not in set"<<endl;
            else{
                for(;i<size-1;++i) elem[i]=elem[i+1];
                size--;
            }
        }
        set &operator=(const set<T> &a){
            if(&a==this) return *this;
            size=a.size;
            volume=a.volume;
            elem=new T[volume];
            for(int i=0;i<size;i++) elem[i]=a.elem[i];
            return *this;
        }
        void bubblesort(){
            int i,j;
            bool flag=false;
            T tmp;
            for(i=1;i<size;i++){
                for(j=0;j<size-i;j++)
                    if(elem[j+1]<elem[j]) {tmp=elem[j];elem[j]=elem[j+1];elem[j+1]=tmp;flag=true;}
                if(!flag) break;
            }
        }
        void display(){     //从小到大输出
            bubblesort();
            for(int i=0;i<size;i++) cout<<elem[i]<<" ";
            cout<<endl;
        }
};


#endif // SET_H_INCLUDED
