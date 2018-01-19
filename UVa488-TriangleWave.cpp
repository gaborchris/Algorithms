//Name: Christian Gabor
//Date: 1/18/19
//Description: Creates a triangle waveform of the amplitude given to it, repreated by the number for frequency
//		Ranked 138 in the UVa online judge running at O(n) time
//		The premade table makes STDOUT much faster, as it can output an entire waveform instead of each character or line
// Easiest to run using: cat input.txt | ./a.out
/* Example input.txt:
2  //number of wavetypes

3  //amplitude
2  //frequecy

5
1
   Output:
1
22
333
22
1

1
22
333
22
1

1
22
333
4444
55555
4444
333
22
1
*/

#include <iostream>
#include <string>

using namespace std;

int main(){


	string table[9] = {
		"1\n",
		"1\n22\n1\n",
		"1\n22\n333\n22\n1\n",
		"1\n22\n333\n4444\n333\n22\n1\n",
		"1\n22\n333\n4444\n55555\n4444\n333\n22\n1\n",
		"1\n22\n333\n4444\n55555\n666666\n55555\n4444\n333\n22\n1\n",
		"1\n22\n333\n4444\n55555\n666666\n7777777\n666666\n55555\n4444\n333\n22\n1\n",
		"1\n22\n333\n4444\n55555\n666666\n7777777\n88888888\n7777777\n666666\n55555\n4444\n333\n22\n1\n",
		"1\n22\n333\n4444\n55555\n666666\n7777777\n88888888\n999999999\n88888888\n7777777\n666666\n55555\n4444\n333\n22\n1\n"};

	int inputs;
	int amp;
	int freq;

	cin>>inputs;

	for(int i = 0; i < inputs-1; i++){
		cin>>amp;
		cin>>freq;
		for(int j = 0; j<freq; j++){
			cout<<table[amp-1]<<endl;
		}
	}

	cin>>amp;
	cin>>freq;

	for(int j = 0; j<freq-1; j++){
		cout<<table[amp-1]<<endl;
	}
	cout<<table[amp-1];

}
