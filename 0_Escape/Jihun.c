#include <stdio.h>
#include <stdlib.h>



typedef struct _Node
{
    int item;
    struct _Node* next;
}Node;
typedef struct _Queue
{
    int size;
    Node* head;
    Node* tail;
}Queue;

Queue* NewQueue()
{
    Queue* q = malloc(sizeof(Queue));
    q->head = NULL;
    q->tail = NULL;
    q->size = 0;
    return q;   //여기 리턴문이 없어도 vscode에서는 정상작동한다. 이유가 뭐지
}
void FreeQueue(Queue* q)
{
    //큐가 비어있지 않을경우
    if(q->size != 0)
    {
        Node* cur = q->head;
        Node* pre = NULL;
        while (cur != NULL)
        {
            pre = cur;
            cur = cur->next;

            free(pre);
        }
    }

    free(q);
}
void EnQueue(Queue* q, int value)
{
    Node* cur = q->tail;
    Node* newNode = malloc(sizeof(Node));
    newNode->item = value;
    newNode->next = NULL;

    q->tail = newNode;
    if(q->size == 0)
    {
        q->head = newNode;
    }
    else
    {
        cur->next = newNode;
    }
    q->size++;
}
int DeQueue(Queue* q)
{
    // 큐에 데이터가 없을 경우 예외처리
    if(q->size == 0) return -1;

    Node* cur = q->head;
    q->size--;
    q->head = cur->next;
    int ret = cur->item;
    free(cur);
    return ret;
}

int CtoI(int i, int j, int C) {return (i*C+j);}

int BFS(int R, int C, char arr[R][C])
{
    Queue* moveQ = NewQueue();
    Queue* waterQ = NewQueue();

    int destI, destJ, cur;

    // 입력받은 보드판 분류
    for(int i = 0; i < R; i++)
    {
        for(int j = 0; j < C; j++)
        {
            cur = arr[i][j];
            if(cur == '*')
            {
                EnQueue(waterQ, CtoI(i,j,C));
            }
            else if(cur == 'S')
            {
                EnQueue(moveQ, CtoI(i,j,C));
            }
            else if(cur == 'D')
            {
                destI = i;
                destJ = j;
            }
        }
    }

    int dx[4] = {0,0,1,-1};
    int dy[4] = {-1,1,0,0};
    int depth = 0;
    //BFS 시작. 큐 2개를 돌려야 하고 목적지 도달 혹은 물에 잠김이라는 완료조건이 있으므로 무한반복문 사용
    while (1)
    {
        depth++;
        int size = moveQ->size;
        if(size == 0)
        {
            FreeQueue(moveQ);
            FreeQueue(waterQ);
            return -1;
        }

        // 무브 BFS
        for(int qIndex = 0; qIndex < size; qIndex++)
        {
            int val = DeQueue(moveQ);
            int i = val/C;
            int j = val%C;
            
            cur = arr[i][j];
            // 해당 위치 물에 잠김
            if(cur == '*') continue;

            for(int d = 0; d < 4; d++)
            {
                int targetI = i+dx[d];
                int targetJ = j+dy[d];
                //도착
                if(targetI == destI && targetJ == destJ) 
                {
                    FreeQueue(moveQ);
                    FreeQueue(waterQ);
                    return depth;
                }

                if(targetI < 0 || targetI >= R || targetJ < 0 || targetJ >= C)  continue;
                if(arr[targetI][targetJ] != '.') continue;
                arr[targetI][targetJ] = depth + '0';
                EnQueue(moveQ, CtoI(targetI, targetJ, C));
            }
        }

        size = waterQ->size;
        // 물 BFS
        for(int qIndex = 0; qIndex < size; qIndex++)
        {
            int val = DeQueue(waterQ);
            int i = val/C;
            int j = val%C;
            
            
            for(int d = 0; d < 4; d++)
            {
                int targetI = i+dx[d];
                int targetJ = j+dy[d];

                if(targetI < 0 || targetI >= R || targetJ < 0 || targetJ >= C)  continue;
                if(arr[targetI][targetJ] == 'X' || arr[targetI][targetJ] == '*' || arr[targetI][targetJ] == 'D') continue;
                arr[targetI][targetJ] = '*';
                EnQueue(waterQ, CtoI(targetI, targetJ, C));
            }
        }

    
        // for(int i = 0; i < R; i++)
        // {
        //     for(int j = 0; j < C; j++)
        //     {
        //         printf("%c", arr[i][j]);
        //     }
        //     printf("\n");
        // }


    }
    
}

int main()
{
    // Queue* q = NewQueue();
    // for(int i = 0; i < 5; i++)
    // {
    //     EnQueue(q, i);
    // }
    // for(int i = 0; i < 6; i++)
    // {
    //     printf("%d ", DeQueue(q));
    // }
    
    // FreeQueue(q);

    int R,C;
    scanf("%d %d", &R, &C);

    char arr[R][C];
    for(int i = 0; i < R; i++)
    {
        char input[C+1]; 
        scanf("%s", input);
        for(int j = 0; j < C; j++)
        {
            arr[i][j] = input[j];
        }
    }
    
    int result = BFS(R,C, arr);
    if(result == -1)
    {
        printf("KAKTUS\n");
    }
    else
    {
        printf("%d\n", result);
    }

    return 0;
}