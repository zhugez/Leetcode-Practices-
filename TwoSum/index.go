package main

// func twoSum(nums []int, target int) []int {
// 	var indexs [2]int
// 	for i := 0; i < len(nums); i++ {
// 		for j := i+1; j < len(nums); j++ {
// 			if nums[i]+nums[j] == target {
// 				return []
// 			}
// 		}
// 	}
func TwoSum(nums []int, target int) []int {
	n := len(nums)
	for i := 0; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			if nums[i]+nums[j] == target {
				return []int{i, j}
			}
		}
	}
	return []int{}
}
func main() {

}
