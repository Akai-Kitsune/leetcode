#include <iostream>
#include <cstdlib>
#include <cstdint>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solition
{
public:
	vector<int> adj[100001]; 
	bool vis[100001]; 
	int low[100001], tin[100001];
	vector<vector<int>> bridge;
	int timer;
	string reverseStr(string s, int k){
		for(int i = 0; i < s.length(); i+=2*k)
            reverse(s.begin() + i, s.begin() + min(int(s.length()), i + k));
        return s;
	}
	void dfs(int node, int par){
		low[node]=tin[node]=timer++;
	    vis[node]=true;
	    for(int child : adj[node]){
	        if(child==par) {
	        	continue;
	        }
	        else if(vis[child]){
	            low[node] = std::min(tin[child], low[node]);
	        } else{
	            dfs(child, node);
	            if(low[child]>tin[node]){
	                // bridge found, add to the answer
	                vector<int> temp; temp.push_back(node); temp.push_back(child);
	                bridge.push_back(temp);
	            }
	            low[node] = std::min(low[child], low[node]);
	        }
    }
}
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        int a,b;
        for(int i=0; i<connections.size(); i++){
            a = connections[i][0];
            b = connections[i][1];
            adj[a].push_back(b); adj[b].push_back(a);
        }

        dfs(0, -1);

        return bridge;
    }
};


