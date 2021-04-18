@.str.0 = private unnamed_addr constant [7 x i8] c"Hello \00", align 1
@.str.1 = private unnamed_addr constant [7 x i8] c"World\0A\00", align 1
@.str.2 = private unnamed_addr constant [7 x i8] c"World\0A\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable
define void @f() {
  %1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.str.0, i64 0, i64 0))
  ret void
}

; Function Attrs: noinline nounwind optnone ssp uwtable
define void @g() {
  %1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.str.1, i64 0, i64 0))
  call void @f()
  %2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.str.2, i64 0, i64 0))
  ret void
}

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  call void @f()
  call void @g()
  %2 = load i32, i32* %1, align 4
  ret i32 %2
}
declare i32 @printf(i8*, ...)