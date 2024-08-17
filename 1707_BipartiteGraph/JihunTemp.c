#include <stdio.h>
#include <stdlib.h>

typedef struct _Vertex
{
    int adjs;
    int color; // 0:접근안함 1,-1 색
}Vertex;

void PrintVertex(Vertex* vertex, int V)
{
    printf("%d : ", vertex->color);
    for(int i = 0; i < V; i++)
    {
        printf("%d ", vertex->adjs);
    }
    printf("\n");
}

void InitVertex(Vertex* vertex, int V)
{
    vertex->adjs = 0;
    vertex->color = 0;
}
void FreeVertex(Vertex* vertex)
{
    free(vertex);
}

int DFS(Vertex* current, int color, int V, Vertex** vertexes)
{
    //색이 이미 있는데 다르면 1반환
    if(current->color != 0)
    {
        if(current->color == color) return 0;
        else return 1;
    }   

    int bitComparer = 1;
    current->color = color;
    for(int i = 0; i < V; i++)
    {
        //current가 탐색할 노드(i)와 인접할 경우 DFS 실행
        if(current->adjs & bitComparer)
        {
            if(DFS(vertexes[i], -color, V, vertexes)) return 1;
        }
        bitComparer <<= 1;
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
            InitVertex(vertexes[i], V);
        }

        // 간선 초기화
        int a, b;
        for(int i = 0; i < E; i++)
        {
            scanf("%d %d", &a, &b);
            vertexes[a-1]->adjs |= (1<<(b-1));
            vertexes[b-1]->adjs |= (1<<(a-1));
        }


        // 입력 완료
        int flag = 1;
        for(int i = 0; i < V; i++)
        {
            Vertex* v = vertexes[i];
            if(v->color != 0) continue;

            if(DFS(v, 1, V, vertexes))
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
        
        for(int i = 0; i < V; i++)
        {
            FreeVertex(vertexes[i]);    // 정점 포인터 해제
        }
        free(vertexes);
    }
}