#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cstring>

#define N 10        //��ĸ�����Ĵ���

char *crossover(char *father,char *mother)   //���溯��������ֵΪ�������Ӵ�
{
    int i,j,k;
    char son[10],rnd[10],fath[10],moth[10];
    for ( i = 0; i < 8; i++){   //���ɽ�������
        rnd[i]=rand()%2+'0';
    }
    strcpy(fath,father);
    strcpy(moth,mother);
    for ( i = 0; i < 8; i ++){    //���ݽ������ӶԸ�ĸ���н���
        if (rnd[i] == '1'){
            for ( j = 0; j < 8; j++){
                if (fath[j] != '0') break;
            }
            son[i]=fath[j];
            for ( k = 0; k < 8; k++){
                if (moth[k] == fath[j]){
                    moth[k]='0';
                    break;
                }
            }
            fath[j]='0';
        }
        else{
            for ( j = 0; j < 8; j++){
                if (moth[j] != '0') break;
            }
            son[i]=moth[j];
            for ( k = 0; k < 8; k++){
                if (fath[k] == moth[j]){
                    fath[k]='0';
                    break;
                }
            }
            moth[j]='0';
        }
    }
    son[8]=0;
    return son;
}

int check(char result[])        //���س�ͻ�Ļʺ����
{
    int i,j,k=0;
    for ( i = 0; i < 8; i++){
        for ( j = i+1; j < 8; j++){
            if (abs(result[i]-result[j]) == j-i) k++;
        }
    }
    return k;
}

int execution(){
    int i,j,k,p,q,min,max=0;
    int flag,sign,boundary=1000;
    int s[N];
    char father[10]="12345678",mother[10]="87654321";
    char son[N][10],temp[10],result[92][10];  //ȡ92����Ϊ��֪��92�ֽⷨ��������N�ʺ�����δ֪�ⷨ�������Խ���ȡ����
    srand(time(NULL));
    for ( i = 0; i < 8; i++){                               //���ɸ�ĸ��
        j=rand()%8;
        k=father[j];
        father[j]=father[i];
        father[i]=k;
        j=rand()%8;
        k=mother[j];
        mother[j]=mother[i];
        mother[i]=k;
    }
    sign=0;
    for ( i = 0; i <= boundary; i++){               //���Ʒ�ֳ����
        if (i == boundary && sign == 1){        //����������������������
            boundary+=3000;
            sign=0;
        }
        for ( j = 0; j < N; j++){                     //����ͱ��� �Ӵ�����
            strcpy(son[j],crossover(mother,father));
            p=rand()%8;
            q=rand()%8;
            k=son[j][p];
            son[j][p]=son[j][q];
            son[j][q]=k;
            s[j]=check(son[j]);
        }
        for ( j = 0; j < N; j++){               //�������������
            for ( k = j, min = j; k < N; k++){
                if (s[min] > s[k]) min=k;
            }
            k=s[j];
            s[j]=s[min];
            s[min]=k;
            strcpy(temp,son[j]);
            strcpy(son[j],son[min]);
            strcpy(son[min],temp);
            if (s[j] == 0){
                flag=0;
                for ( k = 0; k < max; k++){              //�ж��Ƿ����ظ����
                    if (!strcmp(son[j],result[k])) flag=1;
                }
                if (!flag){
                    sign=1;
                    strcpy(result[max],son[j]);           //���ϵķ���������
                    max++;                                    //�Ѿ������ķ���������δ�ظ��Ӵ�
                    //printf("%02d.%s\n",max,son[j]);   //������������ĺ��
                }
            }
        }
        strcpy(father,son[0]);  //ѡ���������ŵĳ�Ϊ��һ���ĸ�ĸ
        strcpy(mother,son[1]);
    }
    //printf("Total perfect generations are %d\n",max); //�õ��������������
    //printf("Final generation is %d\n",boundary);        //���շ�ֳ����
    if(max==92) return 1;
    else if(90<=max) return 2;
    else return 0;
}

int main()
{
    double rate1=0,rate2=0;
    for(int i=0;i<100;i++){  //ʵ��100��
        if(execution()==1) rate1++;
        else if(execution()==2) rate2++;
    }
    printf("Correct rate after 100 expriments:\n");
    printf("Results number is 92: %lf\n",rate1/100);
    printf("Results number between 90 and 92: %lf\n",rate2/100);
    printf("Results number less than 90: %lf\n",(100-rate1-rate2)/100);
    //execution();
    return 0;
}
