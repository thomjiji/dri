- DaVinci Resolve object (MediaPoolItem, TimelineItem, etc.) type annotation
- API 的 calling 方式与原始完全一样，该接受一个 str 作为 arg 就接受 str。
- 这个库只是达芬奇 API 的一个 interface，所以遇到需要 overload 一个 function 的情况，我们可以直接 pass 掉，直接声明两个同名的
  function，不用去管 overload。达芬奇 API 内部已经处理好了 overload。