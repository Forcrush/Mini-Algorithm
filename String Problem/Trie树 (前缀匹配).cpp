#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
using namespace std;
const int MaxN = 26;

//单词的结构
struct Word
{
    char word[100];//单词的内容
    int word_len;//单词的长度
    int ori_id;//单词的原始ID
};

Word dictionary[1000000];//存储字典 后来会排成字典序

//树的节点
struct TrieNode
{
    bool isEnd; //是否是一个单词的结尾字符
    int sonCount; //子节点的个数
    TrieNode* son[MaxN];//子节点指针列表 最多只有26个
    int id;//以此节点字符为结尾的单词 在排序后的字典中的位置
    TrieNode(){
        isEnd = false;
        sonCount = 0;
        id = -1;
        for (int i = 0; i < MaxN; ++i)
            son[i] = NULL;
    }
};

TrieNode* stack[1000000] = {0};//用于DFS的堆栈

TrieNode* root;//根节点 代表整个字典树

//插入一个词 给出词的内容 词的长度 以及 词在单词列表中的位置
void insert(char* word, int len, int id){
    TrieNode* curNode = root;//以根节点为起点
    for (int i = 0; i < len; ++i){
        int index = word[i]-'a';        //index 0~25
        if(curNode->son[index]==NULL){
            curNode->son[index] = new TrieNode();
            curNode->sonCount++;
        }
        if(i==len-1){           //词尾
            curNode->son[index]->isEnd = true;
            curNode->son[index]->id = id;
        }
        curNode = curNode->son[index];
    }
}

int find(int cnt, char* prefix , int len){    //根据前缀查询第cnt个单词 返回在字典中的id
    TrieNode* curNode = root;
    for (int i = 0; i < len; ++i){
        int cid = prefix[i]-'a';
        if(curNode->son[cid] != NULL){
            curNode = curNode->son[cid];
        }
    }
    //已找到了前缀的最后一个字符的节点
    int top = 0;
    stack[top++] = curNode;
    while(top > 0){           //DFS去找第一个该前缀的词
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

bool isIn(Word& word, char* prefix , int len){     //判断单词word是否是以prefix为前缀的
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
    root = new TrieNode();//初始化根节点

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
        //找到以该前缀为前缀的第一个单词(排序后)的 ID 然后+ k-1 判断
        int first = find(k,pre,strlen(pre));

        if(first+k-1 <=N and isIn(dictionary[first+k-1],pre,strlen(pre))) cout<<dictionary[first+k-1].ori_id<<endl;
        else cout<<-1<<endl;
    }
    return 0;
}
