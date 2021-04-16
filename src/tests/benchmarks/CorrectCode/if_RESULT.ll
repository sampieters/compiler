@.str.0 = private unnamed_addr constant [21 x i8] c"Something went wrong\00", align 1
@.str.1 = private unnamed_addr constant [14 x i8] c"Hello world!\0A\00", align 1
@.str.2 = private unnamed_addr constant [14 x i8] c"Hello world!\0A\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  store i32 5, i32* %1, align 4
  %2 = load i32, i32* %1, align 4
  %3 = icmp slt i32 %2, 5
  br i1 %3, label %4, label %6

; <label>:4:
  %5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([21 x i8], [21 x i8]* @.str.0, i64 0, i64 0))
  br label %6

; <label>:6:
  %7 = load i32, i32* %1, align 4
  %8 = icmp sge i32 %7, 5
  br i1 %8, label %9, label %11

; <label>:9:
  %10 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str.1, i64 0, i64 0))
  br label %11

; <label>:11:
  %12 = load i32, i32* %1, align 4
  %13 = icmp eq i32 %12, 5
  br i1 %13, label %14, label %20

; <label>:14:
  %15 = load i32, i32* %1, align 4
  %16 = icmp ne i32 %15, 4
  br i1 %16, label %17, label %19

; <label>:17:
  %18 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str.2, i64 0, i64 0))
  br label %19

; <label>:19:
  br label %20

; <label>:20:
  ret i32 1
}
declare i32 @printf(i8*, ...)