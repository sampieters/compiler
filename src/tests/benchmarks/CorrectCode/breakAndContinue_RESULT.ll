@.str.0 = private unnamed_addr constant [5 x i8] c"%d\n\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() #0 {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  br label %2

; <label>:2:                                                ; preds = %5, %SCOPE VAN WHILE
  %3 = load i32, i32* %1, align 4
  %4 = icmp slt i32%3, 10
  br i1 %4, label %5, label %14

5:                                                ; preds = %2
  %6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.0, i64 0, i64 0), i32 %None)
  %7 = load i32, i32* %1, align 4
  %8 = icmpeq i32%7, 5
  br i1 %8, label %9, label %10

9:                                                ; preds = %SCOPE VAN IF
  br label 14
  br label %10

; <label>:10:                                                ; preds =  %9, %SCOPE VAN IF
  %11 = load i32, i32* %1, align 4
  %12 = add nsw i32%11, 1
  store i32 %12, i32* %1, align 4
  br label 2
  br label %13

; <label>:13:                                                ; preds =  %10, %IF START
  store i32 10, i32* %1, align 4
  br label %2

; <label>:14:                                               ; preds = %2
  ret i32 0
}
declare i32 @printf(i8*, ...) #1