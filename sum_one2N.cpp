#include <iostream>
using namespace std;

// ���� : 1���� N���� M�� �����

/*
# ����
�ڿ��� N�� �ԷµǸ� 1���� N������ �� �� M�� ������� ����ϴ� ���α׷��� �ۼ��ϼ���.

# �Է¼���
ù �ٿ� �ڿ��� N�� M�� ���ʴ�� �Էµ˴ϴ�.(3<=M<N<=1000)

# ��¼���
ù �ٿ� M�� ������� ����Ѵ�.
*/

int main() {
	int n, m, i, sum = 0;
	cin >> n >> m;
	for (i = 1; i <= n; i++) {
		if (i%m == 0) {
			sum = sum + i;
		}
	}

	cout << sum;
	return 0;
}