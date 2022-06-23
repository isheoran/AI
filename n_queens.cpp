#include<iostream>
#include<vector>
using namespace std;

bool is_safe_move(vector<vector<char>>&g,int x,int y,int n) {
    for(int i=0;i<n;i++) {
        if(g[i][y]=='*') return false;
    }
    for(int j=0;j<n;j++) {
        if(g[x][y]=='*') return false;
    }
    for(int i=x,j=y;j<n and i<n;i++,j++) {
        if(g[i][j]=='*') return false;
    }
    for(int i=x,j=y;i>=0 and j>=0;i--,j--) {
        if(g[i][j]=='*') return false;
    }
    for(int i=x,j=y;i>=0 and j<n;i--,j++) {
        if(g[i][j]=='*') return false;
    }
    for(int i=x,j=y;i<n and j>=0;i++,j--) {
        if(g[i][j]=='*') return false;
    }
    return true;
}

bool arrange_queens(vector<vector<char>>&g,int n,int row) {
    if(row>=n) return true;
    for(int i=0;i<n;i++) {
        if(is_safe_move(g,row,i,n)) {
            g[row][i] = '*';
            if(arrange_queens(g,n,row+1)) return true;
            g[row][i] = '.';
        }
    }
    return false;
}

int main() {
    int n;
    cin>>n;
    vector<vector<char>>g(n,vector<char>(n,'.'));
    if(arrange_queens(g,n,0)) {
        for(int i=0;i<n;i++) {
            for(int j=0;j<n;j++) {
                cout<<g[i][j];
            }
            cout<<"\n";
        }
    }
    else {
        cout<<"Note possible to arrange n queens for this configuration of board.";
    }
    return 0;
}