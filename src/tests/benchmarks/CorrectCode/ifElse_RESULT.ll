@.str.0 = private unnamed_addr constant [21 x i8] c"Something went wrong\00", align 1
@.str.1 = private unnamed_addr constant [14 x i8] c"Hello world!\0A\00", align 1
@.str.2 = private unnamed_addr constant [14 x i8] c"Hello world!\0A\00", align 1
@.str.3 = private unnamed_addr constant [21 x i8] c"Something went wrong\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  store i32 5, i32* %1, align 4
  %2 = load i32, i32* %1, align 4
  %3 = icmp slt i32 %2, 5
  br i1 %3, label %4, label %6
; <label>:4:
  %5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([21 x i8], [21 x i8]* @.str.0, i64 0, i64 0))
  br label %8
; <label>:6:
  %7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str.1, i64 0, i64 0))
  br label %8
; <label>:8:
  %9 = load i32, i32* %1, align 4
  %10 = icmp eq i32 %9, 5
  br i1 %10, label %11, label %19
; <label>:11:
  %12 = load i32, i32* %1, align 4
  %13 = icmp eq i32 %12, 5
  br i1 %13, label %14, label %16
; <label>:14:
  %15 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str.2, i64 0, i64 0))
  br label %18
; <label>:16:
  %17 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([21 x i8], [21 x i8]* @.str.3, i64 0, i64 0))
  br label %18
; <label>:18:
  br label %19
; <label>:19:
  ret i32 1
}
declare i32 @printf(i8*, ...)