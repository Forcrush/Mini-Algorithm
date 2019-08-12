#ifndef SEQSTACK_H_INCLUDED
#define SEQSTACK_H_INCLUDED

template<class T>
class seqStack{
    private:
        T *data; //��̬����
        int top_p;//ջ��λ��
        int maxsize;//�����ģ
        void doublespace(){
            T *tmp=data;
            data=new T[2*maxsize];
            for(int i=0;i<maxsize;++i) data[i]=tmp[i];
            maxsize*=2;
            delete [] tmp;
        }
    public:
        seqStack(int initsize=10){
            data=new T[initsize];
            maxsize=initsize;
            top_p=-1;
        }
        ~seqStack() {delete [] data;}
        bool isEmpty() const {return top_p==-1;}
        void push(const T &x){
            if(top_p==maxsize-1) doublespace();
            data[++top_p]=x;
        }
        T pop() {return data[top_p--];}
        T top() {return data[top_p];}
};

#endif // SEQSTACK_H_INCLUDED
