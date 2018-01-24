#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <limits>
#include <ctime>
#include <ratio>
#include <chrono>

#define CONST 10  

void Merge_Sort(int* array, int p, int r);
void Merge(int* array, int p, int q, int r);
void Insertion_Sort(int* a, int b);
void StoogeSort(int* A, int start, int end);

int main(){
	using namespace std::chrono;

	srand(time(NULL));

	int numtrials = 10;

	int size[] = {100, 200, 300, 400, 500, 600, 700, 800, 900, 1000};

	std::cout << "Running Stooge Sorts...\n";
	for(int k = 0; k<numtrials; k++){
		int numbers[size[k]];
		for(int i =0; i<size[k]; i++){
			numbers[i] = rand()%10001;
		}

		high_resolution_clock::time_point t1 = high_resolution_clock::now();

		StoogeSort(numbers, 0, size[k]-1);

		high_resolution_clock::time_point t2 = high_resolution_clock::now();

		duration<double> time_span = duration_cast<duration<double>>(t2 - t1);
		std::cout << "When n = " << size[k] << "\n";
		std::cout << time_span.count() << "\n";


	}

	for(int i = 0; i<numtrials; i++){
		size[i] = size[i]*CONST;
	}
	std::cout << "Running Insertion Sorts...\n";
	for(int k = 0; k<numtrials; k++){
		int numbers[size[k]];
		for(int i =0; i<size[k]; i++){
			numbers[i] = rand()%10001;
		}

		high_resolution_clock::time_point t1 = high_resolution_clock::now();

		Insertion_Sort(numbers, size[k]);

		high_resolution_clock::time_point t2 = high_resolution_clock::now();

		duration<double> time_span = duration_cast<duration<double>>(t2 - t1);
		std::cout << "When n = " << size[k] << "\n";
		std::cout << time_span.count() << "\n";
	}

	for(int i = 0; i<numtrials; i++){
		size[i] = size[i]*CONST;
	}


	std::cout << "Running Merge Sorts...\n";

	for(int k = 0; k<numtrials; k++){
		int numbers[size[k]];
		for(int i =0; i<size[k]; i++){
			numbers[i] = rand()%10001;
		}

		high_resolution_clock::time_point t1 = high_resolution_clock::now();

		Merge_Sort(numbers, 0, size[k] - 1);

		high_resolution_clock::time_point t2 = high_resolution_clock::now();

		duration<double> time_span = duration_cast<duration<double>>(t2 - t1);
		std::cout << "When n = " << size[k] << "\n";
		std::cout << time_span.count() << "\n";
	}
	return 0;
}

void Merge_Sort(int* array, int p, int r){
	if(p < r){
		int q = (p+r)/2;
		Merge_Sort(array, p, q);
		Merge_Sort(array, q + 1 , r);
		Merge(array, p, q, r);
	}
}

void Merge(int* array, int p, int q, int r){

	int n1 = q - p + 1;
	int n2 = r - q;

	int Left[n1 + 1];
	int Right[n2 + 1];

	int i = 0;
	int j = 0;

	for(int i = p; i<n1+p; i++){
		Left[j] = array[i];
		j++;
	}
	Left[j] = std::numeric_limits<int>::max();
	j = 0;
	for(int i = q+1; i<=n2+q; i++){
		Right[j] = array[i];
		j++;
	}
	Right[j] = std::numeric_limits<int>::max();

	i = 0;
	j = 0;
	for(int k = p; k <= r; k++){
		if(Left[i] <= Right[j]){
			array[k] = Left[i];
			i++;
		}
		else{
			array[k] = Right[j];
			j++;
		}
	}
}
void Insertion_Sort(int* array, int length){

	int current_element;
	int j;

	for(int i = 1; i < length; i++){

		current_element = array[i];

		j = i - 1;
		while(j >= 0 && current_element < array[j]){
			array[j+1] = array[j];
			j = j - 1;
		}
		array[j+1] = current_element;
	}
}

void StoogeSort(int* A, int start, int end){
	int n = end - start + 1;
	if(n==2 && A[start] > A[end]){
		int swap;
		swap = A[start];
		A[start] = A[end];
		A[end] = swap;
	}
	if(n>2){
		//ceiling is hard to do in C++ with 2/3, better to invert this
		int m = n/3;
		StoogeSort(A, start, end-m);
		StoogeSort(A, start+m, end);
		StoogeSort(A, start, end-m);
	}
}
