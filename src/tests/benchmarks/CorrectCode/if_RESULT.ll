@.str.0 = private unnamed_addr constant [21 x i8] c"Something went wrong\00", align 1
@.str.1 = private unnamed_addr constant [14 x i8] c"Hello world!\0A\00", align 1
@.str.2 = private unnamed_addr constant [14 x i8] c"Hello world!\0A\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  store i32 5, i32* %2, align 4
  %3 = load i32, i32* %2, align 4
  %4 = icmp slt i32 %3, 5
  br i1 %4, label %5, label %7

; <label>:5:
  %6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([21 x i8], [21 x i8]* @.str.0, i64 0, i64 0))
  br label %7

; <label>:7:
  %8 = load i32, i32* %2, align 4
  %9 = icmp sge i32 %8, 5
  br i1 %9, label %10, label %12

; <label>:10:
  %11 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str.1, i64 0, i64 0))
  br label %12

; <label>:12:
  %13 = load i32, i32* %2, align 4
  %14 = icmp eq i32 %13, 5
  br i1 %14, label %15, label %21

; <label>:15:
  %16 = load i32, i32* %2, align 4
  %17 = icmp ne i32 %16, 4
  br i1 %17, label %18, label %20

; <label>:18:
  %19 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str.2, i64 0, i64 0))
  br label %20

; <label>:20:
  br label %21

; <label>:21:
  %22 = load i32, i32* %1, align 4
  ret i32 %22
}
declare i32 @printf(i8*, ...)