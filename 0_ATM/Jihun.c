#include <stdio.h>


void Merge(int *arr, int *tempArr, int start, int end);
void Sort(int *arr, int *tempArr, int start, int end);


void Sort(int *arr, int *tempArr, int start, int end)
{
    int halfLen = (end-start);
    if(halfLen <= 2)
    {
        if(halfLen == 1)
        {
            tempArr[start] = arr[start];
            return;
        }
        if(arr[start] < arr[start+1])
        {
            tempArr[start] = arr[start];
            tempArr[start+1] = arr[start+1];
        }
        else
        {
            tempArr[start] = arr[start+1];
            tempArr[start+1] = arr[start];
        }
    }
    else
    {
        halfLen /= 2;
        Sort(arr, tempArr, start, end-halfLen);
        Sort(arr, tempArr, end-halfLen, end);
        Merge(arr, tempArr, start, end);
    }
}

void Merge(int *arr, int *tempArr, int start, int end)
{
    int count = end-start;
    int mid = end - (count/2);

    int l = start, r = mid;
    for(int i = 0; i < count; i++)
    {
        if(l >= mid)
        {
            arr[start + i] = tempArr[r];
            r++;
            continue;
        }
        if(r >= end)
        {
            arr[start + i] = tempArr[l];
            l++;
            continue;
        }

        if(tempArr[l] < tempArr[r])
        {
            arr[start + i] = tempArr[l];
            l++;
        }
        else
        {
            arr[start + i] = tempArr[r];
            r++;
        }
    }
    for(int i = start; i < end; i++)
    {
        tempArr[i] = arr[i];
    }
}

int main()
{
    int N;

    scanf("%d", &N);

    int arr[N], tempArr[N];
    for(int i = 0; i < N; i++)
    {
        scanf("%d", &arr[i]);
    }

    Sort(arr, tempArr, 0, N);

    int result = 0;
    for(int i = 0; i < N; i++)
    {
        result += arr[i] * (N-i);
    }
    printf("%d\n", result);
}