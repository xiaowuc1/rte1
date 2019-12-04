#include <iomanip>
#include <ios>
#include <iostream>
#include <vector>
#include "problem.h"

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL); cerr.tie(NULL);
  string s;
  getline(cin, s); // ignore first line, boilerplate
  int n, _, m;
  cin >> n >> _ >> m;
  vector<int> u, v;
  vector<double> w;
  for(int i = 0; i < m; i++) {
    int a, b;
    double c;
    cin >> a >> b >> c;
    u.push_back(a);
    v.push_back(b);
    w.push_back(c);
  }
  cin >> n >> m;
  vector<double> b;
  for(int i = 0; i < n; i++) {
    double t;
    cin >> t;
    b.push_back(t);
  }
  vector<double> ret = FindVoltages(n, u, v, w, b);
  if(ret.size() != n) {
    return 1;
  }
  for(double out: ret) {
    cout << fixed << setprecision(16) << out << "\n";
  }
  return 0;
}
