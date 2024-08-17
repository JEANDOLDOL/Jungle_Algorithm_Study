#include <stdio.h>
void merge(int *list, int left, int mid, int right, int *sorted)
{
    int i, j, k, l;
    i = left;
    j = mid + 1;
    k = left;

    // 분할 정렬된 list의 합병
    while (i <= mid && j <= right)
    {
        if (list[i] <= list[j])
            sorted[k++] = list[i++];
        else
            sorted[k++] = list[j++];
    }

    // 남아 있는 값들을 일괄 복사
    if (i > mid)
    {
        for (l = j; l <= right; l++)
            sorted[k++] = list[l];
    }
    // 남아 있는 값들을 일괄 복사
    else
    {
        for (l = i; l <= mid; l++)
            sorted[k++] = list[l];
    }

    // 배열 sorted[](임시 배열)의 리스트를 배열 list[]로 재복사
    for (l = left; l <= right; l++)
    {
        list[l] = sorted[l];
    }
}
void merge_sort(int *list, int left, int right, int *sorted)
{
    int mid;

    if (left < right)
    {
        mid = (left + right) / 2;
        merge_sort(list, left, mid, sorted);
        merge_sort(list, mid + 1, right, sorted);
        merge(list, left, mid, right, sorted);
    }
}
int main()
{
    int num = 0;
    scanf("%d", &num);
    int arr[num];
    int sorted[num];
    for (int i = 0; i < num; i++)
    {
        scanf("%d", &arr[i]);
    }
    merge_sort(arr, 0, num - 1, sorted);
    for (int i = 0; i < num; i++)
    {
        printf("%d\n", sorted[i]);
    }
    return 0;
}