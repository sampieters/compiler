@.str.0 = private unnamed_addr constant [5 x i8] c"%d\n\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() #0 {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  br label %2

2:                                                ; preds = %5, %SCOPE VAN WHILE
  %3 = load i32, i32* %1, align 4
  %4 = icmp slt i32%3, 10
  br i1 %4, label %5, label %9

5:                                                ; preds = %2
  %6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.0, i64 0, i64 0), i32 %None)
  %7 = load i32, i32* %1, align 4
  %8 = add nsw i32%7, 1
  store i32 %8, i32* %1, align 4
  br label %2

9:                                                ; preds = %2
  ret i32 0
}
declare i32 @printf(i8*, ...) #1