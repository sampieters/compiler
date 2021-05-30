.data
string1_1: .asciiz "Enter a number:\00"
string2_1: .asciiz ""
string2_2: .asciiz "\00"
string3_1: .asciiz "fib("
string3_2: .asciiz ")\t= "
string3_3: .asciiz ";\n\00"
.globl main
.text
                
f:      
        addiu   $sp, $sp, -44
        sw      $fp, 40($sp)
        sw      $ra, 36($sp)
        sw      $4, 32($sp)
        move    $fp, $sp
        sw      $4, 4($fp)
        # BEGIN IF CONDITION
        lw      $8, 4($fp)
        slti    $8, $8, 2
        sw      $8, 8($fp)
        lw      $8, 8($fp)
        beq     $8,$0, $L0
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        lw      $v0, 4($fp)
        j       $FUNC_f
        # END IF BODY
        b       $L1
        nop     
$L0:    
        # BEGIN ELSE BODY
        lw      $8, 4($fp)
        subi    $8, $8, 1
        sw      $8, 12($fp)
        lw      $4, 12($fp)
        jal     f
        sw      $2, 16($fp)
        lw      $8, 4($fp)
        subi    $8, $8, 2
        sw      $8, 20($fp)
        lw      $4, 20($fp)
        jal     f
        sw      $2, 24($fp)
        lw      $8, 16($fp)
        lw      $9, 24($fp)
        add     $10, $8, $9
        sw      $10, 28($fp)
        lw      $v0, 28($fp)
        j       $FUNC_f
        # END ELSE BODY
$L1:    
        li      $v0, 0
        j       $FUNC_f
$FUNC_f:
        move    $sp, $fp
        lw      $4, 32($sp)
        lw      $ra, 36($sp)
        lw      $fp, 40($sp)
        addiu   $sp, $sp, 44
        jr      $ra
                
main:   
        addiu   $sp, $sp, -76
        sw      $fp, 72($sp)
        sw      $ra, 68($sp)
        sw      $4, 64($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $2, 4
        syscall 
        la      $4, string2_1
        li      $2, 4
        syscall 
        lw      $4, 36($fp)
        li      $2, 5
        syscall 
        sw      $v0, 36($fp)
        la      $4, string2_2
        li      $2, 4
        syscall 
        li      $11, 1
        sw      $11, 40($fp)
                
$L2:    
        # BEGIN WHILE CONDITION
        lw      $11, 40($fp)
        lw      $12, 36($fp)
        sle     $11, $11, $12
        sw      $11, 44($fp)
        lw      $11, 44($fp)
        beq     $11, $0, $L3
        nop     
        # END WHILE CONDITION
                
        # BEGIN WHILE BODY
        lw      $11, 40($fp)
        addi    $11, $11, 1
        sw      $11, 48($fp)
        lw      $11, 48($fp)
        sw      $11, 52($fp)
        lw      $11, 52($fp)
        sw      $11, 56($fp)
        lw      $4, 56($fp)
        jal     f
        sw      $2, 60($fp)
        la      $4, string3_1
        li      $2, 4
        syscall 
        lw      $4, 56($fp)
        li      $2, 1
        syscall 
        la      $4, string3_2
        li      $2, 4
        syscall 
        lw      $4, 60($fp)
        li      $2, 1
        syscall 
        la      $4, string3_3
        li      $2, 4
        syscall 
        j       $L2
        # END WHILE BODY
                
$L3:    
        li      $v0, 0
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 64($sp)
        lw      $ra, 68($sp)
        lw      $fp, 72($sp)
        addiu   $sp, $sp, 76
        li      $2, 10
        syscall 