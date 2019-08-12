#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
using namespace std;
const int MaxN = 26;

//���ʵĽṹ
struct Word
{
    char word[100];//���ʵ�����
    int word_len;//���ʵĳ���
    int ori_id;//���ʵ�ԭʼID
};

Word dictionary[1000000];//�洢�ֵ� �������ų��ֵ���

//���Ľڵ�
struct TrieNode
{
    bool isEnd; //�Ƿ���һ�����ʵĽ�β�ַ�
    int sonCount; //�ӽڵ�ĸ���
    TrieNode* son[MaxN];//�ӽڵ�ָ���б� ���ֻ��26��
    int id;//�Դ˽ڵ��ַ�Ϊ��β�ĵ��� ���������ֵ��е�λ��
    TrieNode(){
        isEnd = false;
        sonCount = 0;
        id = -1;
        for (int i = 0; i < MaxN; ++i)
            son[i] = NULL;
    }
};

TrieNode* stack[1000000] = {0};//����DFS�Ķ�ջ

TrieNode* root;//���ڵ� ���������ֵ���

//����һ���� �����ʵ����� �ʵĳ��� �Լ� ���ڵ����б��е�λ��
void insert(char* word, int len, int id){
    TrieNode* curNode = root;//�Ը��ڵ�Ϊ���
    for (int i = 0; i < len; ++i){
        int index = word[i]-'a';        //index 0~25
        if(curNode->son[index]==NULL){
            curNode->son[index] = new TrieNode();
            curNode->sonCount++;
        }
        if(i==len-1){           //��β
            curNode->son[index]->isEnd = true;
            curNode->son[index]->id = id;
        }
        curNode = curNode->son[index];
    }
}

int find(int cnt, char* prefix , int len){    //����ǰ׺��ѯ��cnt������ �������ֵ��е�id
    TrieNode* curNode = root;
    for (int i = 0; i < len; ++i){
        int cid = prefix[i]-'a';
        if(curNode->son[cid] != NULL){
            curNode = curNode->son[cid];
        }
    }
    //���ҵ���ǰ׺�����һ���ַ��Ľڵ�
    int top = 0;
    stack[top++] = curNode;
    while(top > 0){           //DFSȥ�ҵ�һ����ǰ׺�Ĵ�
        TrieNode* toCheck = stack[--top];
        if(toCheck->isEnd) return toCheck->id;
        else{
            int haveAdded = 0;
            for (int i = MaxN-1; i >=0 ; --i){
                if(toCheck->son[i] != NULL){
                    haveAdded++;
                    stack[top++] = toCheck->son[i];
                    if(haveAdded==toCheck->sonCount)
                        break;
                }
            }
        }
    }
    return -1;
}

//bool cmp_int (const int& a, const int& b){
//    return a < b;
//}

bool cmp_word(const Word& a, const Word& b){
    int todo = a.word_len < b.word_len ? a.word_len : b.word_len;
    for (int i = 0; i < todo; ++i){
        if(a.word[i]==b.word[i]) continue;
        return a.word[i] < b.word[i];
    }
    return a.word_len < b.word_len;
}

bool isIn(Word& word, char* prefix , int len){     //�жϵ���word�Ƿ�����prefixΪǰ׺��
    if(word.word_len < len) return false;
    for(int i=0; i < len; i++){
        if(word.word[i] != prefix[i]) return false;
    }
    return true;
}

int main()
{
    int N,M;
    cin>>N>>M;
    root = new TrieNode();//��ʼ�����ڵ�

    for (int i = 1; i <= N; ++i)]{
        scanf("%s",dictionary[i].word);
        dictionary[i].word_len = strlen(dictionary[i].word);
        dictionary[i].ori_id = i;
    }

    sort(dictionary+1, dictionary+N+1, cmp_word);

    for (int i = 1; i <= N; ++i)
        insert(dictionary[i].word, dictionary[i].word_len, i);
    char pre[1000+10];
    for (int i = 0; i < M; ++i){
        int k = 0;
        scanf("%d %s",&k,pre);
        //�ҵ��Ը�ǰ׺Ϊǰ׺�ĵ�һ������(�����)�� ID Ȼ��+ k-1 �ж�
        int first = find(k,pre,strlen(pre));

        if(first+k-1 <=N and isIn(dictionary[first+k-1],pre,strlen(pre))) cout<<dictionary[first+k-1].ori_id<<endl;
        else cout<<-1<<endl;
    }
    return 0;
}
