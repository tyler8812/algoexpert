#include <vector>
#include <iostream>
#include <climits>
using namespace std;

// function declaration
void updateLargest(vector<int> &threeLargest, int num);
void shiftAndUpdate(vector<int> &array, int num, int idx);
vector<int> findThreeLargestNumbers(vector<int> array);

// O(n) time | O(1) space
vector<int> findThreeLargestNumbers(vector<int> array)
{
    vector<int> threeLargest{INT_MIN, INT_MIN, INT_MIN};

    for (int num : array)
    {
        updateLargest(threeLargest, num);
    }
    return threeLargest;
}

void updateLargest(vector<int> &threeLargest, int num)
{
    if (num > threeLargest[2])
    {
        shiftAndUpdate(threeLargest, num, 2);
    }
    else if (num > threeLargest[1])
    {
        shiftAndUpdate(threeLargest, num, 1);
    }
    else if (num > threeLargest[0])
    {
        shiftAndUpdate(threeLargest, num, 0);
    }
}
void shiftAndUpdate(vector<int> &array, int num, int idx)
{

    for (int i = 0; i <= idx; i++)
    {
        if (i == idx)
        {
            array[i] = num;
        }
        else
        {
            array[i] = array[i + 1];
        }
    }
}

int main()
{
    vector<int> array{141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7};
    vector<int> threeLargest = findThreeLargestNumbers(array);
    cout << threeLargest[0] << " " << threeLargest[1] << " " << threeLargest[2] << endl;
    return 0;
}