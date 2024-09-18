# [Silver II] Largest Exotic Number - 21041 

[문제 링크](https://www.acmicpc.net/problem/21041) 

### 성능 요약

메모리: 439236 KB, 시간: 2512 ms

### 분류

브루트포스 알고리즘, 스위핑

### 제출 일자

2024년 9월 18일 18:07:18

### 문제 설명

<ul>
	<li>Athanasios: I have an interesting problem to be proposed for ACM-ICPC INC 2017!</li>
	<li>Berdine: What the problem is about?</li>
	<li>Athanasios: It involves an exotic algorithm.</li>
	<li>Berdine: ... alright, let's hear it!</li>
</ul>

<p>For readability reason, the element of a matrix <em>A</em> at the <em>a</em>-th row and <em>b</em>-th column, <em>A</em><sub><em>a</em>,<em>b</em></sub>, will be written as (<em>a</em>, <em>b</em>). The matrix indices start at 1.</p>

<p>Given a matrix <em>A</em> of size <em>N</em> × <em>N</em>, two elements in the matrix (a, b) and (c, d) are called an exotic pair if all these three conditions are satisfied:</p>

<ol>
	<li>(a, b) and (c, d) have the same value.</li>
	<li>At least one of the following condition is satisfied: a ≠ c, or b ≠ d.</li>
	<li>Both of the following conditions are satisfied: a ≤ c, and b ≤ d.</li>
</ol>

<p>For example, given a matrix:</p>

<pre>3 2 1
5 2 3
4 3 4</pre>

<p>There are four exotic pairs in the matrix:</p>

<ul>
	<li>(1, 1) and (2, 3), of value 3;</li>
	<li>(1, 1) and (3, 2), of value 3;</li>
	<li>(2, 1) and (2, 2), of value 2;</li>
	<li>(3, 1) and (3, 3), of value 4.</li>
</ul>

<p>Among those four exotic pairs, (3, 1) and (3, 3) have the largest value (of 4); we call this kind of number as the largest exotic number.</p>

<p>Your task in this problem is to find the largest exotic number given a matrix, or output -1 if there is no such number.</p>

### 입력 

 <p>The first line contains an integer: <em>N</em> (2 ≤ <em>N</em> ≤ 300) denoting the size of the matrix. The following <em>N</em> lines, each contains <em>N</em> integers (each separated by a single space): <em>A</em><sub><em>i</em>,<em>j</em></sub> (1 ≤ <em>A</em><sub><em>i</em>,<em>j</em></sub> ≤ 100,000) denoting the matrix element at <em>i</em>-th row and <em>j</em>-th column for 1 ≤ <em>i</em> ≤ <em>N</em> and 1 ≤ <em>j</em> ≤ <em>N</em>, respectively.</p>

### 출력 

 <p>The output contains the largest exotic number for the given input, in a line. Output -1 if there is no such number.</p>

