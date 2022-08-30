//시간초과 해결 코드
#include <stdio.h>
#include <string.h>

#pragma warning(disable:4996)

char str[500010];
char d[5000010];
int main()
{

	int a, b;
	scanf("%d %d", &a, &b);

	scanf("%s", str);

	d[0] = str[0];
	int di, si;
	int len = strlen(str);
	for(di = 1, si = 1; si < len; di++,si++){
		while(d[di-1] < str[si] && di > 0 && b > 0){
			d[--di] = '0';
			b--;
		}
		d[di] = str[si];
	}

	if (b > 0) d[di - b] = '\0';

	printf("%s", d);
	return 0;
}
