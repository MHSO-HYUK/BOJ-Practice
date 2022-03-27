#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <tuple>
#include <cstring>

using namespace std;

const int knight_dX[8] = { -2, -2, 2, 2, -1, -1, 1, 1 };
const int knight_dY[8] = { -1, 1, -1, 1, -2, 2, -2, 2 };

const int bishop_dX[4] = { -1, -1, 1, 1 };
const int bishop_dY[4] = { -1, 1, -1, 1 };

const int rook_dX[4] = { -1, 0, 1, 0 };
const int rook_dY[4] = { 0, -1, 0, 1 };

int row, col;

int map[11][11];
bool visited[11][11][111][4];

int locationX[111];
int locationY[111];

const int ROOK = 0;
const int BISHOP = 1;
const int KNIGHT = 2;

const int MAXLIFE = 3;

class chessPiece
{
public:
    int x, y, count, next, pieceType;

    chessPiece(int x, int y, int count, int next, int pieceType)
        :x(x), y(y), count(count), next(next), pieceType(pieceType) {};
};

int min = 987654321;

void bfs(int startX, int startY)
{
    queue<chessPiece> q;

    q.push(chessPiece(startX, startY, 0, 2, ROOK));
    q.push(chessPiece(startX, startY, 0, 2, BISHOP));
    q.push(chessPiece(startX, startY, 0, 2, KNIGHT));

    visited[startX][startY][2][ROOK] = true;
    visited[startX][startY][2][BISHOP] = true;
    visited[startX][startY][2][KNIGHT] = true;

    while (q.empty() == false)
    {
        chessPiece curPiece = q.front();

        int curX = curPiece.x;
        int curY = curPiece.y;
        int count = curPiece.count;
        int next = curPiece.next;
        int pieceType = curPiece.pieceType;

        int nextX = locationX[next];
        int nextY = locationY[next];

        q.pop();

        // 마지막 숫자에 도달한 경우
        if (next == row * col + 1)
        {
            if (::min > count)
                ::min = count;

            return;
        }

        // 말을 바꿈
        for (int i = 0; i < 3; i++)
        {
            if (i == pieceType)
                continue;

            if (visited[curX][curY][next][i])
                continue;

            visited[curX][curY][next][i] = true;
            q.push(chessPiece(curX, curY, count + 1, next, i));
        }

        // 현재 말이 룩 일때
        if (pieceType == ROOK)
        {
            for (int i = 0; i < 4; i++)
            {
                for (int offset = 1; ; offset++)
                {
                    int nX = curX + rook_dX[i] * offset;
                    int nY = curY + rook_dY[i] * offset;

                    if (nX < 0 || nX >= row || nY < 0 || nY >= col)
                        break;

                    if (visited[nX][nY][next][ROOK])
                        continue;

                    visited[nX][nY][next][ROOK] = true;

                    if (nX == nextX && nY == nextY)
                    {
                        q.push(chessPiece(nX, nY, count + 1, next + 1, ROOK));
                    }
                    else
                        q.push(chessPiece(nX, nY, count + 1, next, ROOK));
                }
            }
        }
        // 현재 말이 비숍 일때
        else if (pieceType == BISHOP)
        {
            for (int i = 0; i < 4; i++)
            {
                for (int offset = 1; ; offset++)
                {
                    int nX = curX + bishop_dX[i] * offset;
                    int nY = curY + bishop_dY[i] * offset;

                    if (nX < 0 || nX >= row || nY < 0 || nY >= col)
                        break;

                    if (visited[nX][nY][next][BISHOP])
                        continue;

                    visited[nX][nY][next][BISHOP] = true;

                    if (nX == nextX && nY == nextY)
                    {
                        q.push(chessPiece(nX, nY, count + 1, next + 1, BISHOP));
                    }
                    else
                        q.push(chessPiece(nX, nY, count + 1, next, BISHOP));
                }
            }
        }
        // 현재 말이 비숍 일때
        else if (pieceType == KNIGHT)
        {
            for (int i = 0; i < 8; i++)
            {
                int nX = curX + knight_dX[i];
                int nY = curY + knight_dY[i];

                if (nX < 0 || nX >= row || nY < 0 || nY >= col)
                    continue;

                if (visited[nX][nY][next][KNIGHT])
                    continue;

                visited[nX][nY][next][KNIGHT] = true;

                if (nX == nextX && nY == nextY)
                {
                    q.push(chessPiece(nX, nY, count + 1, next + 1, KNIGHT));
                }
                else
                    q.push(chessPiece(nX, nY, count + 1, next, KNIGHT));
            }
        }


    }
}

void solve()
{
    int startX = -1, startY = -1;

    for (int i = 0; i < row; i++)
        for (int j = 0; j < col; j++)
            if (map[i][j] == 1)
            {
                startX = i, startY = j;
                break;
            }

    bfs(startX, startY);

    cout << ::min << endl;
}

int main()
{
    memset(visited, false, sizeof(visited));

    cin >> row;	col = row;

    for (int i = 0; i < row; i++)
        for (int j = 0; j < col; j++)
        {
            cin >> map[i][j];

            locationX[map[i][j]] = i;
            locationY[map[i][j]] = j;
        }

    solve();

    return 0;
}