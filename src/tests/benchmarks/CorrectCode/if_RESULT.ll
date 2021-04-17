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
  %15 = zext i1 %14 to i32
  %16 =  i32 %15 to i32
  %14 = icmp ne i32 %16, 1
  br i1 %16, label %17, label %23

; <label>:17:
  %18 = load i32, i32* %1, align 4
  %19 = icmp ne i32 %18, 4
  br i1 %19, label %20, label %22

; <label>:20:
  %21 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str.2, i64 0, i64 0))
  br label %22

; <label>:22:
  br label %23

; <label>:23:
  ret i32 1
}
declare i32 @printf(i8*, ...)