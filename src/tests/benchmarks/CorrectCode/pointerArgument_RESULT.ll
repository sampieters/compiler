@.str.0 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
@.str.2 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.str.3 = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
@.str.4 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.str.5 = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
@.str.6 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.str.7 = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable
define void @f(i32*) {
  %2 = alloca i32*, align 8
  store i32* %0, i32** %2, align 8
  %3 = load i32*, i32** %2, align 8
  %4 = load i32, i32* %3, align 4
  %5 = add nsw i32 %4, 1
  store i32 %5, i32* %3, align 4
  ret void
}

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  store i32 0, i32* %2, align 4
  %3 = alloca i32*, align 8
  store i32* %2, i32** %3, align 8
  %4 = load i32*, i32** %3, align 8
  store i32 42, i32* %4, align 4
  %5 = load i32, i32* %2, align 4
  %6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.0, i64 0, i64 0), i32 %5)
  %7 = load i32*, i32** %3, align 8
  %8 = load i32, i32* %7, align 4
  %9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.1, i64 0, i64 0), i32 %8)
  %10 = load i32*, i32** %3, align 8
  %11 = load i32, i32* %10, align 4
  %12 = add nsw i32 %11, 1
  store i32 %12, i32* %10, align 4
  %13 = load i32, i32* %2, align 4
  %14 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.2, i64 0, i64 0), i32 %13)
  %15 = load i32*, i32** %3, align 8
  %16 = load i32, i32* %15, align 4
  %17 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.3, i64 0, i64 0), i32 %16)
  call void @f(i32* %2)
  %18 = load i32, i32* %2, align 4
  %19 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.4, i64 0, i64 0), i32 %18)
  %20 = load i32*, i32** %3, align 8
  %21 = load i32, i32* %20, align 4
  %22 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.5, i64 0, i64 0), i32 %21)
  %23 = load i32*, i32** %3, align 8
  call void @f(i32* %23)
  %24 = load i32, i32* %2, align 4
  %25 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.6, i64 0, i64 0), i32 %24)
  %26 = load i32*, i32** %3, align 8
  %27 = load i32, i32* %26, align 4
  %28 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.7, i64 0, i64 0), i32 %27)
  %29 = load i32, i32* %1, align 4
  ret i32 %29
}
declare i32 @printf(i8*, ...)