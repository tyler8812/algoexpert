#include <vector>
#include <iostream>
using namespace std;
// O(n + m) time | O(1) space
vector<int> searchInSortedMatrix(vector<vector<int>> matrix, int target)
{
    int row = 0;
    int col = matrix[0].size() - 1;
    while (row < matrix.size() && col >= 0)
    {
        cout << row << col << endl;
        if (target > matrix[row][col])
        {
            row++;
        }
        else if (target < matrix[row][col])
        {
            col--;
        }
        else
        {
            return {row, col};
        }
    }
    return {-1, -1};
}
int main()

{
    vector<vector<int>> matrix{
        {1, 4, 7, 12, 15, 1000},
        {2, 5, 19, 31, 32, 1001},
        {3, 8, 24, 33, 35, 1002},
        {40, 41, 42, 44, 45, 1003},
        {99, 100, 103, 106, 128, 1004}};
    int target = 44;
    vector<int> answer;
    answer = searchInSortedMatrix(matrix, target);
    cout << answer[0] << " " << answer[1] << endl;
    return 0;
};