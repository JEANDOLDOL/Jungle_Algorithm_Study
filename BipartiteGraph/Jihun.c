#include <stdio.h>
#include <stdlib.h>

typedef struct _Vertex Vertex;  // 구조체를 사용하기 위해 미리 선언

typedef struct _Node
{
    Vertex* vertex;
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
    int index;
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

void PrintVertex(Vertex* vertex)
{
    printf("%d : ", vertex->color);
    
    Node* node = vertex->adjs->root;
    if(node)
    {
        printf("%d ", node->vertex->index);
        while (node->next)
        {
            // next = node->next;
            node = node->next;
            printf("%d ", node->vertex->index);
        }
    }
    printf("\n");
}

void InitVertex(Vertex* vertex, int V, int index)
{
    vertex->adjs = (LinkedList*)malloc(sizeof(LinkedList));
    vertex->adjs->root = NULL;
    vertex->adjs->last = NULL;
    vertex->color = 0;
    vertex->index = index;
}
void FreeVertex(Vertex* vertex)
{
    Node* node = vertex->adjs->root;
    Node* next = NULL;
    if(node)
    {
        while (node->next)
        {
            next = node->next;
            free(node);
            node = next;
        }
    }
    
    free(vertex->adjs);
    free(vertex);
}

int DFS(Vertex* current, int color, int V)
{
    //색이 이미 있는데 다르면 1반환
    if(current->color != 0)
    {
        if(current->color == color) return 0;
        else return 1;
    }

    current->color = color;

    Node* target = current->adjs->root;
    while (target)
    {
        //target에 대해 DFS 실행
        if(DFS(target->vertex, -color, V)) return 1;
        target = target->next;
    }
    return 0;
}

int main()
{
    int testCount;
    scanf("%d", &testCount);
    for(int i = 0; i < testCount; i++)
    {
        int V, E;
        scanf("%d %d", &V, &E);

        Vertex** vertexes = calloc(V, sizeof(Vertex*));

        // 정점 초기화
        for(int i = 0; i < V; i++)
        {
            vertexes[i] = (Vertex*)malloc(sizeof(Vertex));  //정점 포인터 동적할당
            InitVertex(vertexes[i], V, i);
        }

        // 간선 초기화
        int a, b;
        for(int i = 0; i < E; i++)
        {
            scanf("%d %d", &a, &b);
            AddAdj(vertexes[a-1],vertexes[b-1]);
        }


        // 입력 완료
        int flag = 1;
        for(int i = 0; i < V; i++)
        {
            Vertex* v = vertexes[i];
            if(v->color != 0) continue;

            if(DFS(v, 1, V))
            {
                flag = 0;
                printf("NO\n");
                break;
            }
        }
        
        if(flag)
        {
            printf("YES\n");
        }

        // for(int i = 0; i < V; i++)
        // {
        //     printf("{%d} ", i);
        //     PrintVertex(vertexes[i]);    // 정점 포인터 해제
        // }
        
        for(int i = 0; i < V; i++)
        {
            FreeVertex(vertexes[i]);    // 정점 포인터 해제
        }
        free(vertexes);
    }
}