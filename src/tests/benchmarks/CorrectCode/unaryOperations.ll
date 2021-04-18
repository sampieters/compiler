; ModuleID = 'src/tests/benchmarks/CorrectCode/unaryOperations.c'
source_filename = "src/tests/benchmarks/CorrectCode/unaryOperations.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str = private unnamed_addr constant [5 x i8] c"%d; \00", align 1

; Function Attrs: noinline nounwind optnone uwtable
define i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca [2 x i32], align 4
  store i32 0, i32* %1, align 4
  store i32 9, i32* %2, align 4
  %4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str, i32 0, i32 0), i32 9)
  %5 = load i32, i32* %2, align 4
  %6 = add nsw i32 %5, 1
  store i32 %6, i32* %2, align 4
  %7 = load i32, i32* %2, align 4
  %8 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str, i32 0, i32 0), i32 %7)
  %9 = getelementptr inbounds [2 x i32], [2 x i32]* %3, i64 0, i64 0
  store i32 15, i32* %9, align 4
  %10 = getelementptr inbounds [2 x i32], [2 x i32]* %3, i64 0, i64 1
  store i32 12, i32* %10, align 4
  store i32 12, i32* %2, align 4
  %11 = getelementptr inbounds [2 x i32], [2 x i32]* %3, i64 0, i64 1
  %12 = load i32, i32* %11, align 4
  %13 = add nsw i32 %12, -1
  store i32 %13, i32* %11, align 4
  %14 = getelementptr inbounds [2 x i32], [2 x i32]* %3, i64 0, i64 1
  %15 = load i32, i32* %14, align 4
  %16 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str, i32 0, i32 0), i32 %15)
  %17 = load i32, i32* %2, align 4
  %18 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str, i32 0, i32 0), i32 %17)
  %19 = load i32, i32* %2, align 4
  %20 = add nsw i32 %19, 1
  store i32 %20, i32* %2, align 4
  %21 = load i32, i32* %2, align 4
  %22 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str, i32 0, i32 0), i32 %21)
  %23 = getelementptr inbounds [2 x i32], [2 x i32]* %3, i64 0, i64 0
  %24 = load i32, i32* %23, align 4
  %25 = add nsw i32 %24, -1
  store i32 %25, i32* %23, align 4
  %26 = getelementptr inbounds [2 x i32], [2 x i32]* %3, i64 0, i64 0
  %27 = load i32, i32* %26, align 4
  %28 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str, i32 0, i32 0), i32 %27)
  ret i32 1
}

declare i32 @printf(i8*, ...) #1

attributes #0 = { noinline nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 6.0.0-1ubuntu2 (tags/RELEASE_600/final)"}
