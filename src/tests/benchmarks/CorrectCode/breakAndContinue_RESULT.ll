
; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  br label %2

; <label>:2:
  %3 = load i32, i32* %1, align 4
  %4 = icmp slt i32 %3, 10
  br i1 %4, label %5, label %13

; <label>:5:
  %6 = load i32, i32* %1, align 4
  %7 = icmp eq i32 %6, 5
  br i1 %7, label %8, label %9

; <label>:8:
  br label %13
  br label %9

; <label>:9:
  %10 = load i32, i32* %1, align 4
  %11 = add nsw i32 %10, 1
  store i32 %11, i32* %1, align 4
  br label %2
  br label %12

; <label>:12:
  store i32 10, i32* %1, align 4
  br label %2

; <label>:13:
  ret i32 0
}