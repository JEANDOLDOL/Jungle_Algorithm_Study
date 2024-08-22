#include <stdio.h>
#include <stdlib.h>


typedef struct _Vertex Vertex;  // 구조체를 사용하기 위해 미리 선언

typedef struct _Node
{
    Vertex* vertex;
    int cost;
    struct _Node* next;  // struct 키워드를 사용해 Node 구조체를 명시
} Node;

typedef struct _LinkedList
{
    Node* root;
    Node* last;

} LinkedList;

struct _Vertex
{
    LinkedList* adjs;
    int color; // 0:접근안함 1,-1 색
    //int index;
};

void AddAdj(Vertex* a, Vertex* b)
{
    Node* aAdj = (Node*)malloc(sizeof(Node));
    aAdj->vertex = b;
    aAdj->next = NULL;
    Node* cur = a->adjs->last;
    if(cur == NULL)
    {
        a->adjs->root = aAdj;
        a->adjs->last = aAdj;
    }
    else
    {
        cur->next = aAdj;
        a->adjs->last = aAdj;
    }
    
    
    Node* bAdj = (Node*)malloc(sizeof(Node));
    bAdj->vertex = a;
    bAdj->next = NULL;
    cur = b->adjs->last;
    if(cur == NULL)
    {
        b->adjs->root = bAdj;
        b->adjs->last = bAdj;
    }
    else
    {
        cur->next = bAdj;
        b->adjs->last = bAdj;
    }
    
}


int main()
{
    int M,N,a,b,c;
    scanf("%d", &N);
    scanf("%d", &M);

    Vertex **vertexes = calloc(sizeof(Vertex), N);
    for(int i = 0; i < N; i++)
    {
        InitVertex(vertexes[i], N);
    }

    // 간선 입력
    for(int i = 0; i < M; i++)
    {
        scanf("%d %d %d", &a, &b, &c);

        int cur = vertexes[a]->adjs[b];
        if(cur != -1 && cur < c)
            continue;
        vertexes[a]->adjs[b] = c;
        vertexes[b]->adjs[a] = c;
    }

    // 출발점, 도착점 입력
    scanf("%d %d", &a, &b);

    return 0;
}