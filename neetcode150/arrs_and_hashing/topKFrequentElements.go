package main

func main() {

}

func topKFrequent(nums []int, k int) []int {
	// count frequency of each element using hashing
	var m = make(map[int] int)
	for var i = 0; i < len(nums); i++ {
		m[nums[i]] += 1
	}



}